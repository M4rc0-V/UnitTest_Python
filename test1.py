from unittest import TestCase, main
from zeros import zeros

class zerosTestCase(TestCase):
    def test_1_begin_zeros(self):
        self.assertEqual(zeros([0,0,0,1,2,3]),[1,2,3,0,0,0])
    def test_2_end_zeros(self):
        self.assertEqual(zeros([1,2,3,4,5,0,0,0]),[1,2,3,4,5,0,0,0])
    def test_3_empty(self):
        self.assertEqual(zeros([]),[])
    def test_4_no_zeros(self):
        self.assertEqual(zeros([1,2,3,4,5]),[1,2,3,4,5])
    def test_4_only_zeros(self):
        self.assertEqual(zeros([0,0,0,0,0]),[0,0,0,0,0])
    def test_4_middle_zeros(self):
        self.assertEqual(zeros([1,2,0,0,0,3,4]),[1,2,3,4,0,0,0])


if __name__ == '__main__':
    main()
