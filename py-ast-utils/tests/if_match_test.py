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

    def testBasicIf(self):
        node = create_node.If(
            create_node.Name('True'))
        string = """if True:\n  pass\n"""
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testBasicIfElse2(self):
        node = create_node.If(
            create_node.Name('True'), orelse=[create_node.Pass()])
        string = """if True:\n  pass\nelse:\n  pass\n"""
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testBasicIfElif(self):
        node = create_node.If(
            create_node.Name('True'),
            orelse=[create_node.If(create_node.Name('False'))])
        string = """if True:
  pass
elif False:
  pass
"""
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testIfElifWithSpace(self):
        node = create_node.If(
            create_node.Name('True'),
            orelse=[create_node.If(create_node.Name('False'))])
        string = """if True:
  pass

elif False:
  pass
"""
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testIfInElse(self):
        node = create_node.If(
            create_node.Name('True'),
            orelse=[create_node.If(create_node.Name('False'))])
        string = """if True:
  pass
else:
  if False:
    pass
"""
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testIfAndOthersInElse(self):
        node = create_node.If(
            create_node.Name('True'),
            orelse=[create_node.If(create_node.Name('False')),
                    create_node.Expr(create_node.Name('True'))])
        string = """if True:
  pass
else:
  if False:
    pass
  True
"""
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

