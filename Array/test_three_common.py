import unittest
import three_common

class Teststockpro(unittest.TestCase):

    def test_comman_element(self):
        self.assertEqual(three_common.comman_element([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]),[20, 80])
        self.assertEqual(three_common.comman_element([1, 1, 2, 5, 9],[1,2,3,4,5,5],[1,3,5,7,9]),[1,5])

if __name__ == '__main__':
    unittest.main()