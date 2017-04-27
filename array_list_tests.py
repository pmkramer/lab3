import unittest
from array_list import *

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
        pass
    def test_add(self):
        pass
    def test_length(self):
        pass
    def test_get(self):
        pass
    def test_set(self):
        pass
    def test_remove(self):
        pass

if __name__ == '__main__':
    unittest.main()
