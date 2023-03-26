import unittest

import create_node
import source_match


class ArgumentsMatcherTest(unittest.TestCase):

    def testEmpty(self):
        node = create_node.arguments()
        string = ''
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testSingleArg(self):
        node = create_node.arguments(args=['a'])
        string = 'a'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testMultipleArgs(self):
        node = create_node.arguments(args=['a', 'b'])
        string = 'a, b'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testDefault(self):
        node = create_node.arguments(args=['a'], defaults=['b'])
        string = 'a=b'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testDefaults(self):
        node = create_node.arguments(args=['a', 'c'], defaults=['b', 'd'])
        string = 'a=b, c=d'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testArgsAndDefaults(self):
        node = create_node.arguments(
            args=['e', 'f', 'a', 'c'], defaults=['b', 'd'])
        string = 'e, f, a=b, c=d'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        matched_source = matcher.GetSource()
        self.assertEqual(string, matched_source)

    def testArgsDefaultsVarargs(self):
        node = create_node.arguments(
            args=['e', 'f', 'a', 'c'], defaults=['b', 'd'],
            vararg='args')
        string = 'e, f, a=b, c=d, *args'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testArgsDefaultsVarargsKwargs(self):
        node = create_node.arguments(
            args=['e', 'f', 'a', 'c'], defaults=['b', 'd'],
            vararg='args', kwarg='kwargs')
        string = 'e, f, a=b, c=d, *args, **kwargs'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())
