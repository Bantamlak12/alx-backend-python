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
        """  Parameterizes a unit test """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
