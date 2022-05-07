import unittest
import best_stock

class Teststockpro(unittest.TestCase):

    def test_best_profit(self):
        self.assertEqual(best_stock.best_profit([7,1,5,3,6,4]),5)
        self.assertEqual(best_stock.best_profit([7,6,4,3,1]),0,)

if __name__ == '__main__':
    unittest.main()