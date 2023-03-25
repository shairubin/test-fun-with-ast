import unittest

import create_node
import source_match


class IfMatcherTest(unittest.TestCase):
    def testSimpleIfElse(self):
        node = create_node.If(conditional=True, body=[create_node.Pass()], orelse=[create_node.Pass()])
        string = 'if       True:   \n pass    \nelse:\n pass \n'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        matcher_source = matcher.GetSource()
        self.assertEqual(string, matcher_source)

    def testSimpleIfElseWithCommentAndSpeacses(self):
        node = create_node.If(conditional=True, body=[create_node.Pass()], orelse=[create_node.Pass()])
        string = 'if       True: #comment  \n pass    \nelse: # comment    \n pass#comment\n'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        matcher_source = matcher.GetSource()
        self.assertEqual(string, matcher_source)

    def testSimpleIf(self):
        node = create_node.If(conditional=True, body=[create_node.Pass()])
        string = 'if       True:\n pass         \n'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        matcher_source = matcher.GetSource()
        self.assertEqual(string, matcher_source)
