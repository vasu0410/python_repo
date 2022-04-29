import unittest
import max_min_ary

class Testmaxmin(unittest.TestCase):

    def test_maxmin(self):
        self.assertEqual(max_min_ary.maxmin([1,2,3,4,5,6,7,8,9]),f'9 1')
        self.assertEqual(max_min_ary.maxmin([100,52,77,80,32,9,24]),f'100 9')

if __name__ == '__main__':
    unittest.main()