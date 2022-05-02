import unittest
import dup_array

class Testdup(unittest.TestCase):

    def test_dup_array(self):
        self.assertEqual(dup_array.duplicate_arr([1,3,4,2,2]),2)
        self.assertEqual(dup_array.duplicate_arr([3,3,1,2,4,5,6]),3)

if __name__ == '__main__':
   
    unittest.main()
