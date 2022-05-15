import unittest
import sub_product

class Testproduct(unittest.TestCase):

    def test_subprodcut(self):
        self.assertEqual(sub_product.sub_product([6, -3, -10, 0, 2]),180)
        self.assertEqual(sub_product.sub_product([2, 3, 4, 5, -1, 0]),120)

if __name__ == '__main__':
    unittest.main()        
