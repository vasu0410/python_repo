import unittest
import max_subary

class Testsubary(unittest.TestCase):

    def test_max_sub_array(self):
        self.assertEqual(max_subary.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]),4)
        self.assertEqual(max_subary.max_sub_array([-1,-2,-5,-6]),-1)

if __name__ == '__main__':
    unittest.main()