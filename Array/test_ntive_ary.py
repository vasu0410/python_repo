import unittest
import ntive_ary

class Testntive(unittest.TestCase):

    def test_ntive(self):
        self.assertEqual(ntive_ary.ntary([-12,-13,1,-2,22,42,-6]),[-12,-13,-2,-6,1,22,42])
        self.assertEqual(ntive_ary.ntary([1,2,-3,5,-6,-7,8,-9]),[-3,-6,-7,-9,1,2,5,8])

if __name__ == '__main__':
    unittest.main()
