import unittest
import kadanes_algo

class Testkadans(unittest.TestCase):

    def test_kadan_algo(self):
        self.assertEqual(kadanes_algo.kadan_algo([-2, 1, -3, 4, -1, 2, 1, -5, 4]),6)
        self.assertEqual(kadanes_algo.kadan_algo([-1,-2,-5,-6]),-1)

if __name__ == '__main__':
    unittest.main()