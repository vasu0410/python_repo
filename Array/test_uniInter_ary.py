import unittest
import uniInter_ary

class TestuniInt(unittest.TestCase):

    def test_union(self):
        self.assertEqual(uniInter_ary.union_array([1,2,3,4,5],[1,2,4]),5)
        self.assertEqual(uniInter_ary.union_array([85,25,1,32,54,6],[85,2]),7)


    def test_intersection(self):
        self.assertEqual(uniInter_ary.itersection_array([1,2,3,4,5],[1,2,4]),3)
        self.assertEqual(uniInter_ary.itersection_array([85,25,1,32,54,6],[85,2]),1)

if __name__ == '__main__':
    unittest.main()