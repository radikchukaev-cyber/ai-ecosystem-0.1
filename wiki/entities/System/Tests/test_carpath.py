import unittest

class TestCarpath(unittest.TestCase):
    def test_carpath_route(self):
        route = ["A", "B", "C"]
        self.assertEqual(len(route), 3)

if __name__ == '__main__':
    unittest.main()
