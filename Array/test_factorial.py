import unittest
import factorial

class Testfactorial(unittest.TestCase):

    def test_fact(self):
        self.assertEqual(factorial.fact(5),120)
        self.assertEqual(factorial.fact(10),3628800)

if __name__ == '__main__':
    unittest.main()        
