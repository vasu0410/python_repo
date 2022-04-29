import unittest
import rvr_ary

class Testrvr(unittest.TestCase):

    def test_indx(self):
        self.assertEqual(rvr_ary.indx([1,2,3,4,5]),[5,4,3,2,1])
        self.assertEqual(rvr_ary.indx(['p','y','t','h','o','n']),['n','o','h','t','y','p'])
        

if __name__ == '__main__':
    unittest.main()        