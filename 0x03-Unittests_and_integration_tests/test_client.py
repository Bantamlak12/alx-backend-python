#!/usr/bin/env python3
"""
File: test_client
"""
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ Unit tests """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org, get_response):
        """ Tests the org method """
        get_response.return_value = {'result': 'Success'}
        client = GithubOrgClient(org)
        result = client.org
        url = f'https://api.github.com/orgs/{org}'
        get_response.assert_called_once_with(url)
        self.assertEqual(result, {'result': 'Success'})

    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos_url(self, mock_property):
        """ Mocking a property """
        mock_property.return_value = "https://api.github.com/orgs/google/repos"
        obj = GithubOrgClient('google')
        result = obj._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")
        mock_property.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Tests GithubOrgClient.public_repos """

        mock_get_json.return_value = [{"name": "Repo1"}, {"name": "Repo2"}]

        mock = 'client.GithubOrgClient._public_repos_url'
        with patch(mock, new_callable=PropertyMock,
                   return_value="https://example.com") as mock_url:
            c = GithubOrgClient('google')
            result = c.public_repos()
            self.assertEqual(result, ["Repo1", "Repo2"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://example.com")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, l_key, expected):
        """ Tests has_license_key method """
        self.assertEqual(GithubOrgClient.has_license(repo, l_key), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
    )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test: fixtures """

    @classmethod
    def setUpClass(cls):
        """ Set up class for integration test """
        cls.get_patcher = patch('requests.get')
        with cls.get_patcher('requests.get') as mock_get:
            mock_response = Mock()
            mock_get.json.side_effect = [cls.org_payload, cls.repos_payload]
            mock_get.return_value = mock_response
            cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls):
        """ Tear down class after intergration test """
        cls.get_patcher.stop()
