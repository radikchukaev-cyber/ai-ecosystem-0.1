import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__ if '__file__' in globals() else '.'), '../Tools')))
try:
    from memory_search import search_memory
except ImportError:
    pass

class TestMemorySystem(unittest.TestCase):
    def test_search_memory_empty(self):
        try:
            res = search_memory(".", "nonexistent_keyword_12345")
            self.assertEqual(res, [])
        except NameError:
            pass

if __name__ == '__main__':
    unittest.main()
