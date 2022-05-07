import unittest
import mrg_intervals

class Testmrg(unittest.TestCase):

    def test_mrg_interval(self):

        self.assertEqual(mrg_intervals.mrg_interval([[1,3],[2,6],[8,10],[15,18]]),[[1,6],[8,10],[15,18]])
        self.assertEqual(mrg_intervals.mrg_interval([[1,4],[4,5]]),[[1,5]])
        self.assertEqual(mrg_intervals.mrg_interval([[1,3]]),[[1,3]])
        

if __name__ == '__main__':

    unittest.main()        
