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
        ('google', {'message': 'success'}),
        ('abc', {'message': 'success'})
    ])
    def test_org(self, org, get_response):
        """ Tests the org method """
        with patch('client.get_json') as mock_get_json:
            mock_get_json.return_value = get_response

            client = GithubOrgClient(org)
            result = client.org

            self.assertEqual(result, get_response)

            mock_get_json.assert_called_once_with(
                    f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """ Mocking a property """
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) \
                as mock_org:
            expected = 'https://api.github.com/orgs/google/repos'
            mock_org.return_value = {'repos_url': expected}
            client = GithubOrgClient('google')

            result = client._public_repos_url

            self.assertEqual(result, expected)
            mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Tests GithubOrgClient.public_repos """

        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        mock_get_json.return_value = mock_payload

        expected_repos = ['repo1', 'repo2']
        test_url = 'https://api.github.com/orgs/google/repos'

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_url:
            mock_url.return_value = test_url

            client = GithubOrgClient('google')
            result = client.public_repos()

            self.assertEqual(result, expected_repos)
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(test_url)

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
    """ Integration test: all internal logic are allow to run naturally.
        Only request.get() is mocked since it is external API.
    """

    @classmethod
    def setUpClass(cls):
        """ Set up class for integration test """
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        # Simulate .json() behavior
        def side_effect(url):
            mock_response = Mock()
            if url == GithubOrgClient.ORG_URL.format(org="google"):
                mock_response.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                mock_response.json.return_value = cls.repos_payload
            return mock_response

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """ Tear down class after intergration test """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Tests public_repos """
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """ Tests public_repos method with argument license=\"apache-2.0\" """
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)
