import unittest
import sum_pair

class Testsumpair(unittest.TestCase):

    def test_best_profit(self):
        self.assertEqual(sum_pair.sum_pair([1,5,7,1],6),2)
        self.assertEqual(sum_pair.sum_pair([1,1,1,1],2),6,)

if __name__ == '__main__':
    unittest.main()