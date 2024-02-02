#!/usr/bin/env python3
"""
File: test_utils.py
"""
from utils import access_nested_map, get_json
from parameterized import parameterized, parameterized_class
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


@parameterized_class([
    {"url": "http://example.com", "payload": {"payload": True}},
    {"url": "http://holberton.io", "payload": {"payload": False}}
])
class TestGetJson(unittest.TestCase):
    """ Mock HTTP Calls """

    @patch('requests.get')
    def test_get_json(self, mock_get):
        """Test the get_json function with different URL and payloads."""
        mock_response = Mock()
        mock_response.json.return_value = self.payload
        mock_get.return_value = mock_response

        result = get_json(self.url)

        mock_get.assert_called_once_with(self.url)
        self.assertEqual(result, self.payload)


if __name__ == '__main__':
    unittest.main()
