#!/usr/bin/env python3
""" Unittests for utils.py """

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized

from typing import (
    Dict,
    Mapping,
    Sequence,
    Tuple,
    Union,
)

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """ Tests the `access_nested_map` function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Union[Dict, int]
            ) -> None:
        """ Tests `access_nested_map`'s output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nestedMap: Mapping,
            pathMap: Sequence,
            exc: Exception,
            ) -> None:
        """ Tests `access_nested_map`'s exception handling."""
        with self.assertRaises(exc):
            access_nested_map(nestedMap, pathMap)


class TestGetJson(unittest.TestCase):
    """Tests the `get_json` function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            testURL: str,
            testingPayload: Dict,
            ) -> None:
        """Tests `get_json`'s output."""

        attributes = {'json.return_value': testingPayload}

        with patch("requests.get", return_value=Mock(**attributes)) as req_get:
            self.assertEqual(get_json(testURL), testingPayload)
            req_get.assert_called_once_with(testURL)


class TestMemoize(unittest.TestCase):
    """ Tests the `memoize` decorator."""
    def test_memoize(self) -> None:
        """ Tests the `memoize` decorator."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as a_b:
            testClass = TestClass()
            self.assertEqual(testClass.a_property(), 42)
            self.assertEqual(testClass.a_property(), 42)
            a_b.assert_called_once()
