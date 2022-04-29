import unittest
import kth_minMax

class Testkth(unittest.TestCase):

    def test_kth(self):
        self.assertEqual(kth_minMax.kth_maxMin([7,10,4,3,20,15],3),f'10 7')
        self.assertEqual(kth_minMax.kth_maxMin([3,2,3,1,2,4,5,5,6],4),f'4 3')

if __name__ == '__main__':
    unittest.main()        

