import unittest
import rearrange_pos_neg

class Testreposneg(unittest.TestCase):

    def test_best_profit(self):
        self.assertEqual(rearrange_pos_neg.rearrange_pos_neg([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]),[-5, 5, -2, 2, -8, 4, 7, 1, 8, 0])
        self.assertEqual(rearrange_pos_neg.rearrange_pos_neg([-4, 1, -1, 2, 3, 4]),[-4, 1, -1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()