import unittest
import sort_ary

class Testsort(unittest.TestCase):

    def test_sort(self):
        self.assertEqual(sort_ary.sortary([0,1,0]),[0,0,1])
        self.assertEqual(sort_ary.sortary([0,2,1,2,0]),[0,0,1,2,2])

if __name__ == '__main__':
    unittest.main()        
