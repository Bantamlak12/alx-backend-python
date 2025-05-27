#!/usr/bin/env python3
"""
File: test_utils.py
"""
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ Provides a unit test """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ Testing for value Equality. Parametrized unit test """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested, path):
        """ Testing for a KeyError with context manager"""
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


class TestMemoize(unittest.TestCase):
    """ Unit test for memoize decorator """

    def test_memoize(self):
        """ Test memoization """

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_instance = TestClass()
            mock_a_method.return_value = 42

            # Call the method twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Assert a_method was called only once
            mock_a_method.assert_called_once()

            # Assert if the results are equal
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
