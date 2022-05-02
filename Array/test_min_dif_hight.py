import unittest
import min_dif_hight

class Testdif(unittest.TestCase):

    def test_min_hight(self):
        self.assertEqual(min_dif_hight.min_hight([8 ,1 ,5 ,4 ,7 ,5 ,7 ,9 ,4 ,6],5),8)
        self.assertEqual(min_dif_hight.min_hight([1, 5, 8, 10],2),5)

if __name__ == '__main__':
    unittest.main()


