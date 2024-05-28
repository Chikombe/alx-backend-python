#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class
"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from typing import Dict
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
        org_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}

        # Patch the org property of GithubOrgClient to return the known payload
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = org_payload

            # Instantiate GithubOrgClient
            client = GithubOrgClient("test_org")

            # Call the _public_repos_url method
            result = client._public_repos_url

            # Define the expected URL based on the known payload
            expected_url = "https://api.github.com/orgs/google/repos"

            # Assert that the result matches the expected URL
            self.assertEqual(result, expected_url)

            # Assert that the org property was accessed once
            mock_org.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests the `public_repos` method."""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    @patch('client.get_json')
    def test_has_license(self, repo, license_key, expected_result,
                         mock_get_json):
        """
        Test has_license method of GithubOrgClient
        """
        # Set up mock response
        mock_get_json.return_value = repo

        # Instantiate GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call the has_license method
        result = client.has_license(repo, license_key)

        # Assert that the result matches the expected value
        self.assertEqual(result, expected_result)

        # Assert that get_json method was called once
        mock_get_json.assert_called_once()


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos',
                      'apache2_repos'),
                     [(org_payload, repos_payload, expected_repos,
                       apache2_repos)])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test cases for the GithubOrgClient class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class
        """
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Side effect to return different payloads based on URL
        cls.mock_get.side_effect = [
            Mock(json=lambda: cls.org_payload),
            Mock(json=lambda: cls.repos_payload)
        ]

    @classmethod
    def tearDownClass(cls):
        """
        Clean up after the test class
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method of GithubOrgClient
        """
        # Instantiate GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call the public_repos method
        result = client.public_repos

        # Assert that the result matches the expected list of repositories
        self.assertEqual(result, self.expected_repos)

    def test_has_license_apache2(self):
        """
        Test has_license method of GithubOrgClient with Apache 2 license
        """
        # Instantiate GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call the has_license method with Apache 2 license
        result = client.has_license(self.repos_payload, "apache-2.0")

        # Assert that the result is True for Apache 2 license
        self.assertTrue(result)
