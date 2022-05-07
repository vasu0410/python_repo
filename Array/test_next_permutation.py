import unittest
import next_permutation

class Testnxt(unittest.TestCase):

    def test_mrg_interval(self):

        self.assertEqual(next_permutation.next_permutation([1,2,3]),[1,3,2])
        self.assertEqual(next_permutation.next_permutation([3,2,1]),[1,2,3])
        self.assertEqual(next_permutation.next_permutation([1,1,5]),[1,5,1])
        

if __name__ == '__main__':

    unittest.main()        
