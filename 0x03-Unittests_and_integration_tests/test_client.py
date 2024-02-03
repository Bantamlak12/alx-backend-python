#!/usr/bin/env python3
"""
File: test_client
"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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
