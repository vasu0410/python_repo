import unittest
import consecutive_subsequence

class Testconseq(unittest.TestCase):

    def test_conseq(self):
        self.assertEqual(consecutive_subsequence.con_squence([2,6,1,9,4,5,3]),6)
        self.assertEqual(consecutive_subsequence.con_squence([1,9,3,10,4,20,2]),4)

if __name__ == '__main__':
    unittest.main()        
