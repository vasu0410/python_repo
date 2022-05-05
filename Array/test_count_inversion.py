import unittest
import count_inversion

class Testcountinv(unittest.TestCase):

    def test_count_inversion(self):

        self.assertEqual(count_inversion.count_inversion([2, 4, 1, 3, 5]),3)
        self.assertEqual(count_inversion.count_inversion([2, 3, 4, 5, 6]),0)
        self.assertEqual(count_inversion.count_inversion([10,10,10]),0)
        

if __name__ == '__main__':

    unittest.main()        
