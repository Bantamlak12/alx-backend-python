#!/usr/bin/env python3
"""
File: test_utils.py
"""
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ Provides a unit test """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ Testing for value Equality """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested, path, result):
        """ Testing for a key Error """
        if result == KeyError:
            with self.assertRaises(KeyError):
                access_nested_map(nested, path)


class TestGetJson(unittest.TestCase):
    """ Mock HTTP Calls """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Test the get_json function with different URL and payloads."""
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = payload
            mock_get.return_value = mock_response

            result = get_json(url)

        mock_get.assert_called_once_with(url)
        self.assertEqual(result, payload)
