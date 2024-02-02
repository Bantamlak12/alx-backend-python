#!/usr/bin/env python3
"""
File: test_utils.py
"""
from parameterized import parameterized
import unittest

access_nested_map = __import__('utils').access_nested_map


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
