#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Dict
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for the GithubOrgClient class
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """
        Test that GithubOrgClient.org returns the correct value
        """
        expected_url = f"https://api.github.com/orgs/{org_name}"
        test_payload: Dict = {"org_name": org_name}

        # Set up mock response
        mock_get_json.return_value = test_payload

        # Instantiate GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Assert that get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(expected_url)

        # Assert that the result matches the test payload
        self.assertEqual(result, test_payload)
