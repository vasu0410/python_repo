import unittest
import mrg_array

class Testmrg(unittest.TestCase):

    def test_mrg_arr(self):

        self.assertEqual(mrg_array.mrg_arr([1,3,5,7],[0,2,6,8,9]),[0,1,2,3,5,6,7,8,9])
        self.assertEqual(mrg_array.mrg_arr([10,12],[5,18,20]),[5,10,12,18,20])

if __name__ == '__main__':
    unittest.main()