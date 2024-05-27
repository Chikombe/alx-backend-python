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

    def test_public_repos_url(self):
        """
        Test _public_repos_url method of GithubOrgClient
        """
        # Define a known payload for org method
        org_payload = {"public_repos": 5}

        # Patch the org property of GithubOrgClient to return the known payload
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = org_payload

            # Instantiate GithubOrgClient
            client = GithubOrgClient("test_org")

            # Call the _public_repos_url method
            result = client._public_repos_url

            # Define the expected URL based on the known payload
            expected_url = f"https://api.github.com/orgs/test_org/repos?per_page=5&page=1"

            # Assert that the result matches the expected URL
            self.assertEqual(result, expected_url)

            # Assert that the org property was accessed once
            mock_org.assert_called_once()
