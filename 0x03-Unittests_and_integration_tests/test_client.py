#!/usr/bin/env python3
"""
File: test_client
"""
from client import GithubOrgClient, get_json
from parameterized import parameterized
from unittest.mock import patch
import client
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
