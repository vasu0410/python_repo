import unittest
import min_jump

class Testminjump(unittest.TestCase):

    def test_min_jump(self):
        self.assertEqual(min_jump.min_jump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]),3)
        self.assertEqual(min_jump.min_jump([2, 3, 1, 1, 2, 4, 2, 0, 1, 1]),4)

if __name__ == '__main__':

    unittest.main()