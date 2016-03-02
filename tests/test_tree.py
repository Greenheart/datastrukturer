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
        self.assertTupleEqual(bt.lookup(3), (3, "three"))  # Node with a value
        self.assertTupleEqual(bt.lookup(5), (5, None))
        self.assertTupleEqual(bt.lookup(7), (7, None))
        self.assertTupleEqual(bt.lookup(8), (8, None))
        self.assertIsNone(bt.lookup(9001))

    def test_delete(self):
        """Basic tests of the delete-method."""
        bt = BinarySearchTree(10)
        self.assertFalse(bt.delete(7))  # You can't delete non-existing nodes

        # It's possible to delete children that lack own children
        bt.insert(2)
        self.assertTrue(bt.delete(2))
        self.assertIsNone(bt.lookup(2))

        # It's possible to delete a node that have one other child
        #     10
        #    /
        #   3
        #    \
        #     4
        bt.insert(3)
        bt.insert(4)
        self.assertTrue(bt.delete(3))
        self.assertEqual(bt.left.key, 4)    # 4 should still be a child to root

        # It's possible to delete a node on the right side of the parent
        bt.insert(11)
        self.assertTrue(bt.delete(11))
        self.assertIsNone(bt.right)

        # Delete a node (on the right side of root) that have own children
        bt.insert(15)
        bt.insert(14)
        self.assertTrue(bt.delete(15))
        self.assertEqual(bt.right.key, 14)
        self.assertIsNone(bt.lookup(15))

    def test_delete_node_with_large_subtree(self):
        """Delete nodes with subtrees larger than one node."""
        #         5
        #        /
        #       4   <-- This should be deleted
        #      /
        #     2
        #    / \
        #   1   3
        bt = BinarySearchTree(5)
        bt.insert(4)
        bt.insert(2)
        bt.insert(1)
        bt.insert(3)

        self.assertTrue(bt.delete(4))
        self.assertIsNone(bt.lookup(4))

        # Verify that the other nodes are intact
        self.assertEqual(bt.key, 5)
        self.assertEqual(bt.left.key, 2)
        self.assertEqual(bt.left.left.key, 1)
        self.assertEqual(bt.left.right.key, 3)

    def test_delete_node_on_right_side_of_parent_with_large_subtree(self):
        """Delete nodes with subtrees larger than one node."""
        #         0
        #          \
        #           2   <-- This should be deleted
        #         /  \
        #        1    5
        #            / \
        #           4   6   <-- 4 should replace 2
        bt = BinarySearchTree(0)
        bt.insert(2)
        bt.insert(1)
        bt.insert(5)
        bt.insert(4)
        bt.insert(6)

        self.assertTrue(bt.delete(2))
        self.assertIsNone(bt.lookup(2))

        # Verify that the other nodes are intact
        self.assertEqual(bt.key, 0)
        self.assertEqual(bt.right.key, 4)
        self.assertEqual(bt.right.left.key, 1)
        self.assertEqual(bt.right.right.key, 5)
        self.assertIsNone(bt.right.right.left)
        self.assertEqual(bt.right.right.right.key, 6)

    def test_delete_root_node(self):
        """It should be possible to delete the root node."""
        #         5   <-- This should be deleted
        #        / \
        #       2   7  <-- This should replace the deleted 5
        #      / \
        #     1   3
        bt = BinarySearchTree(5)
        bt.insert(7)
        bt.insert(2)
        bt.insert(1)
        bt.insert(3)
        self.assertTrue(bt.delete(5))
        self.assertIsNone(bt.lookup(5))

        self.assertEqual(bt.key, 7)  # 7 is the new root
        self.assertEqual(bt.left.key, 2)
        self.assertEqual(bt.left.left.key, 1)

    def test_delete_node_with_large_subtree_and_two_children(self):
        """It should be possible to delete nodes that have two children."""
        #         5
        #        /
        #       2   <-- This should be deleted
        #      / \
        #     1   3   <-- This should replace the deleted 2
        bt = BinarySearchTree(5)
        bt.insert(2)
        bt.insert(1)
        bt.insert(3)
        self.assertTrue(bt.delete(2))

        # Verify that the other nodes are intact
        self.assertEqual(bt.key, 5)
        self.assertEqual(bt.left.key, 3)
        self.assertEqual(bt.left.left.key, 1)

    def test_delete_node_with_large_subtree_and_two_large_children(self):
        """Delete node with large subtree consisting of large children.

        It should be possible to delete nodes that have two children which
        in turn have large subtrees
        """
        #              20
        #             /
        #            2   <-- This should be deleted
        #          /   \
        #         1     5
        #       /      /  \
        #     -1      4    11
        #            /   /   \
        #           3   9    13     <-- 3 should replace the deleted 2
        #                \
        #                 10
        bt = BinarySearchTree(20)
        bt.insert(2)
        bt.insert(1)
        bt.insert(-1)

        bt.insert(5)
        bt.insert(4)
        bt.insert(3)

        bt.insert(11)
        bt.insert(9)
        bt.insert(10)
        bt.insert(13)

        self.assertTrue(bt.delete(2))

        # Verify that the other nodes are intact
        self.assertEqual(bt.key, 20)
        self.assertEqual(bt.left.key, 3)
        self.assertEqual(bt.left.left.key, 1)
        self.assertEqual(bt.left.left.left.key, -1)

        self.assertEqual(bt.left.right.key, 5)
        self.assertEqual(bt.left.right.left.key, 4)
        self.assertIsNone(bt.left.right.left.left)  # 3 should replace 2
        self.assertEqual(bt.left.right.right.key, 11)
        self.assertEqual(bt.left.right.right.left.key, 9)
        self.assertEqual(bt.left.right.right.left.right.key, 10)
        self.assertEqual(bt.left.right.right.right.key, 13)
