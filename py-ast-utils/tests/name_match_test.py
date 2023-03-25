import unittest

import pytest

import create_node
import source_match


class NameMatcherTest(unittest.TestCase):

    def testBasicMatch(self):
        node = create_node.Name('foobar')
        string = 'foobar'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testBasicMatchWithWS(self):
        node = create_node.Name('foobar')
        string = ' \t  foobar \t'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testBasicMatchWithWSAndComment(self):
        node = create_node.Name('foobar')
        string = ' \t  foobar \t #comment'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testBasicMatchOnlyComment(self):
        node = create_node.Name('foobar')
        string = ' \t  foobar#comment'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testBasicMatchOnlyComment(self):
        node = create_node.Name('foobar')
        string = ' \t #comment  foobar'
        matcher = source_match.GetMatcher(node)
        with pytest.raises(source_match.BadlySpecifiedTemplateError):
            matcher.Match(string)

    def testIdChange(self):
        node = create_node.Name('foobar')
        string = 'foobar'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        node.id = 'hello'
        self.assertEqual('hello', matcher.GetSource())
