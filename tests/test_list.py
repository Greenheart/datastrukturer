import unittest
from exercises.list import Node, UnorderedList
from exercises.exceptions import *


class NodeTests(unittest.TestCase):

    def test_node(self):
        self.assertEqual(Node(5, None).data, 5)


class UnorderedListTests(unittest.TestCase):

    def test_size(self):
        ul = UnorderedList()
        ul.add(5)
        self.assertLess(ul.size(), 2)
        ul.add(8)
        self.assertEqual(ul.size(), 2)


    def test_is_empty(self):
        ul = UnorderedList()
        self.assertTrue(ul.is_empty())
        ul.add(4)
        self.assertFalse(ul.is_empty())


    def test_search(self):
        ul = UnorderedList()
        ul.add(5)
        ul.add(4)
        ul.add(6)
        self.assertFalse(ul.search(7))
        ul.add(7)
        ul.add(8)
        self.assertTrue(ul.search(7))


    def test_remove(self):
        ul = UnorderedList()
        self.assertRaises(EmptyList, ul.remove, 5)
        ul.add(5)
        ul.add(6)
        self.assertFalse(ul.remove(4))
        self.assertTrue(ul.remove(5))
        self.assertEqual(ul.size(), 1)
        self.assertTrue(ul.remove(6))


    def test_index(self):
        ul = UnorderedList()
        ul.add(5)
        ul.add(4)
        ul.add(5)
        ul.add(6)
        self.assertRaises(IndexError, ul.index, 8)
        self.assertEqual(ul.index(5), 1)


    def test_insert(self):
        ul = UnorderedList()
        self.assertTrue(ul.insert(0, 4))
        ul.add(5)
        ul.add(3)
        self.assertTrue(ul.insert(2, 5))
        self.assertTrue(ul.insert(0, 8))
        self.assertTrue(ul.search(5))
        self.assertRaises(IndexError, ul.insert, 8, 100)


    def test_pop(self):
        ul = UnorderedList()
        self.assertRaises(EmptyList, ul.pop)  # It's not possible to pop from empty lists
        ul.add(1)
        self.assertRaises(IndexError, ul.pop, -1)  # Index out of range
        self.assertRaises(IndexError, ul.pop, 200)  # Index out of range
        self.assertListEqual(ul._vals(), [1])

        ul.add(2)
        ul.add(3)
        ul.add(4)
        ul.add(5)

        self.assertEqual(ul.index(5), 0)
        self.assertListEqual(ul._vals(), [5, 4, 3, 2, 1])
        self.assertEqual(ul.pop(4), 1)  # Pop last item using index
        self.assertListEqual(ul._vals(), [5, 4, 3, 2])
        self.assertEqual(ul.pop(0), 5)  # Pop first
        self.assertListEqual(ul._vals(), [4, 3, 2])
        self.assertEqual(ul.pop(), 2)
        self.assertEqual(ul.pop(0), 4)
        self.assertListEqual(ul._vals(), [3])

        self.assertEqual(ul.pop(), 3)   # Pop last item without index
        self.assertEqual(ul.size(), 0)
        ul.add(1)
        self.assertEqual(ul.pop(0), 1)  # Pop last item using index


    def test_append(self):
        ul = UnorderedList()
        self.assertTrue(ul.append(5))
        self.assertEqual(ul.size(), 1)
        self.assertTrue(ul.append("a"))
        self.assertEqual(ul.size(), 2)
        self.assertTrue(ul.append('b'))
        self.assertTrue(ul.append('c'))
        self.assertTrue(ul.append('d'))
