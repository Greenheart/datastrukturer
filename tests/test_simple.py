import unittest
from exercises.simple import Stack, Queue


class StackTests(unittest.TestCase):

    def test_push(self):
        s = Stack()
        self.assertTrue(s.push(5))

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(5)
        self.assertFalse(s.is_empty())

    def test_size(self):
        s = Stack()
        s.push(5)
        s.push(6)
        self.assertEqual(s.size(), 2)
        s.push(123123123)
        self.assertEqual(s.size(), 3)

    def test_pop(self):
        s = Stack()
        s.push(3)
        s.push("a")
        self.assertEqual(s.pop(), "a")
        self.assertEqual(s.pop(), 3)

    def test_peek(self):
        s = Stack()
        s.push(3)
        s.push('a')
        self.assertEqual(s.peek(), 'a')
        self.assertNotEqual(s.peek(), 3)

class QueueTests(unittest.TestCase):
    pass
