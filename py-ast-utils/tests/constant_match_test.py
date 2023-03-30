import unittest

import pytest

import create_node
import source_match


class NumMatcherTest(unittest.TestCase):

    def testBasicMatch(self):
        node = create_node.Num('1')
        string = '1'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        matched_string = matcher.GetSource()
        self.assertEqual(string, matched_string)

    def testBasicMatchWithPlusSign(self):
        node = create_node.Num('1')
        string = '+1'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        matched_string = matcher.GetSource()
        self.assertEqual(string, matched_string)

    def testBasicMatchWithMinusSign(self):
        node = create_node.Num('-1')
        string = '-1'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        matched_string = matcher.GetSource()
        self.assertEqual(string, matched_string)

    def testBasicMatchWithMinusSignAndWS(self):
        node = create_node.Num('1')
        string = '   1   '
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        matched_string = matcher.GetSource()
        self.assertEqual(string, matched_string)

    def testMatchWSWithComment(self):
        node = create_node.Num('1')
        string = '   1   #comment'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        matched_string = matcher.GetSource()
        self.assertEqual(string, matched_string)

    def testWithParans(self):
        node = create_node.Num('1')
        string = '(1)'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        matched_string = matcher.GetSource()
        self.assertEqual(string, matched_string)

    def testLargeNumberMatch(self):
        node = create_node.Num('1234567890987654321')
        string = '1234567890987654321'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testBasicNoMatch(self):
        node = create_node.Num('2')
        string = '1'
        matcher = source_match.GetMatcher(node)
        with pytest.raises(source_match.BadlySpecifiedTemplateError):
            matcher.Match(string)
