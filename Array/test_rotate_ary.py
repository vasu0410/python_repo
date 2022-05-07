import unittest
import rotate_ary

class Testrotate(unittest.TestCase):

    def test_rotate(self):
        self.assertEqual(rotate_ary.rotaAry([9,8,7,6,4,2,1,3]),[3,9,8,7,6,4,2,1])
        self.assertEqual(rotate_ary.rotaAry([1]),[1])

if __name__ == '__main__':
    unittest.main()        
