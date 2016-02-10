import unittest
from exercises.tree import BinarySearchTree


class TreeNodeTests(unittest.TestCase):
    pass


class TreeTests(unittest.TestCase):
    def test_insert(self):
        bt = BinarySearchTree(5)
        self.assertTrue(bt.insert(2))
        self.assertTrue(bt.insert(3))

    def test_lookup(self):
        #        5
        #      /  \
        #    2    8
        #   / \  /
        #  1  3 7

        bt = BinarySearchTree(5)
        bt.insert(2)
        bt.insert(1)
        bt.insert(3, "three")
        bt.insert(8)
        bt.insert(7)
        self.assertTupleEqual(bt.lookup(1), (1, None))
        self.assertTupleEqual(bt.lookup(2), (2, None))
        self.assertTupleEqual(bt.lookup(3), (3, "three"))   # This node was given a value
        self.assertTupleEqual(bt.lookup(5), (5, None))
        self.assertTupleEqual(bt.lookup(7), (7, None))
        self.assertTupleEqual(bt.lookup(8), (8, None))
        self.assertIsNone(bt.lookup(9001))
