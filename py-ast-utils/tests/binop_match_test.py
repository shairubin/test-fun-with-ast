import unittest

import create_node
import source_match


class BinOpMatcherTest(unittest.TestCase):

    def testAddBinOp(self):
        node = create_node.BinOp(
            create_node.Name('a'),
            create_node.Add(),
            create_node.Name('b'))
        string = 'a + c'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testSubBinOp(self):
        node = create_node.BinOp(
            create_node.Name('a'),
            create_node.Sub(),
            create_node.Name('b'))
        string = 'a - b'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testMultBinOp(self):
        node = create_node.BinOp(
            create_node.Name('a'),
            create_node.Mult(),
            create_node.Name('b'))
        string = 'a * b'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testDivBinOp(self):
        node = create_node.BinOp(
            create_node.Name('a'),
            create_node.Div(),
            create_node.Name('b'))
        string = 'a / b'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testFloorDivBinOp(self):
        node = create_node.BinOp(
            create_node.Name('a'),
            create_node.FloorDiv(),
            create_node.Name('b'))
        string = 'a // b'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testModBinOp(self):
        node = create_node.BinOp(
            create_node.Name('a'),
            create_node.Mod(),
            create_node.Name('b'))
        string = 'a % b'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testPowBinOp(self):
        node = create_node.BinOp(
            create_node.Name('a'),
            create_node.Pow(),
            create_node.Name('b'))
        string = 'a ** b'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testLShiftBinOp(self):
        node = create_node.BinOp(
            create_node.Name('a'),
            create_node.LShift(),
            create_node.Name('b'))
        string = 'a << b'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testRShiftBinOp(self):
        node = create_node.BinOp(
            create_node.Name('a'),
            create_node.RShift(),
            create_node.Name('b'))
        string = 'a >> b'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testBitOrBinOp(self):
        node = create_node.BinOp(
            create_node.Name('a'),
            create_node.BitOr(),
            create_node.Name('b'))
        string = 'a | b'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testBitXorBinOp(self):
        node = create_node.BinOp(
            create_node.Name('a'),
            create_node.BitXor(),
            create_node.Name('b'))
        string = 'a ^ b'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())

    def testBitAndBinOp(self):
        node = create_node.BinOp(
            create_node.Name('a'),
            create_node.BitAnd(),
            create_node.Name('b'))
        string = 'a & b'
        matcher = source_match.GetMatcher(node)
        matcher.Match(string)
        self.assertEqual(string, matcher.GetSource())
