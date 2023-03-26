import unittest

import create_node
import source_match


class NumMatcherTest(unittest.TestCase):

    def testBasicMatch(self):
        node = create_node.Num('1')
        string = '1'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testBasicMatchWithSign(self):
        node = create_node.Num('2')
        string = '+1'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

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
        matcher.Match(string)
        self.assertNotEqual('1', matcher.GetSource())

    # not supported in python 3
    # def testBasicMatchWithSuffix(self):
    #     node = create_node.Num('1')
    #     string = '1L'
    #     matcher = source_match.GetMatcher(node)
    #     matcher.Match(string)
    #     self.assertEqual('1L', matcher.GetSource())
