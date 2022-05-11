import unittest
import subarray_zero

class Testsubarray(unittest.TestCase):

    def test_rotate(self):
        self.assertEqual(subarray_zero.subarray_zero([4, 2, 0, 1, 6]),'Yes')
        self.assertEqual(subarray_zero.subarray_zero([4, 2, -3, 1, 6]),'Yes')

if __name__ == '__main__':
    unittest.main()        
