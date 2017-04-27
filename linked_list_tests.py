import unittest
from linked_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)

        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)
    def test_empty_list(self):
        self.assertEqual(empty_list() is None, True)
    def test_add(self):
        list1 = Pair("hello", None)
        ret_l1 = Pair("hello", Pair("world", None))
        ret_l2 = Pair("world", Pair("hello", None))
        self.assertEqual(add(list1, 0, "world"), ret_l2)
        self.assertEqual(add(list1, 1, "world"), ret_l1)
        self.assertEqual(add(None, 0, "world"), Pair('world', None))
        self.assertRaises(IndexError, add, list1, 2, "world")
        self.assertRaises(IndexError, add, list1, -1, "world")
        self.assertRaises(IndexError, add, None, 1, "world")
    def test_length(self):
        self.assertEqual(length(None), 0)
        self.assertEqual(length(Pair(1, None)), 1)
        self.assertEqual(length(Pair(1, Pair("2", None))), 2)
    def test_get(self):
        self.assertEqual(get(Pair(1, None), 0), 1)
        self.assertEqual(get(Pair(1, Pair("hello", Pair("awesome", None))), 1), "hello")
        self.assertRaises(IndexError, get, None, 0)
        self.assertRaises(IndexError, get, Pair(1, None), -1)
        self.assertRaises(IndexError, get, Pair(1, None), 1)
    def test_set(self):
        self.assertEqual(set(Pair(1, Pair(2, None)), 1, 1.5), Pair(1, Pair(1.5, None)))
        self.assertEqual(set(Pair(1, None), 0, "hello"), Pair("hello", None))
        self.assertRaises(IndexError, set, None, -1, "world")
        self.assertRaises(IndexError, set, None, 1, "world")
        self.assertRaises(IndexError, set, Pair(1, None), 2, "world")
    def test_remove(self):
        self.assertEqual(remove(Pair(1, None), 0), (1, None))
        self.assertEqual(remove(Pair(1, Pair("hello", Pair("goodbye", Pair("end", None)))), 2), ("goodbye", Pair(1, Pair("hello", Pair("end", None)))))
        self.assertRaises(IndexError, remove, None, 0)
        self.assertRaises(IndexError, remove, Pair(1, None), 1)
        self.assertRaises(IndexError, remove, Pair(1, None), -1)
if __name__ == '__main__':
    unittest.main()
