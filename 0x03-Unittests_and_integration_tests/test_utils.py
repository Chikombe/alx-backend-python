#!/usr/bin/env python3
"""
Unit tests for utils module
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Dict
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for the access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map with various inputs and expected outputs
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map raises KeyError for invalid paths
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """
    Test cases for the get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test get_json returns the expected result
        """
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test cases for the memoize decorator
    """

    class TestClass:
        """
        Test class with a_method and a_property decorated with memoize
        """

        def a_method(self):
            """
            Sample method to be memoized
            """
            return 42

        @memoize
        def a_property(self):
            """
            Property using memoize decorator
            """
            return self.a_method()

    def test_memoize(self):
        """
        Test memoization behavior
        """
        # Create an instance of TestClass
        test_instance = self.TestClass()

        # Patch the a_method of TestClass with a mock
        with patch.object(test_instance, 'a_method') as mock_method:
            # Call the memoized property twice
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

            # Assert that the mock method was called only once
            mock_method.assert_called_once()

            # Assert that the results of both calls are the same
            self.assertEqual(result1, result2)
