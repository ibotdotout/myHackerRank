import unittest
import utopian_tree as ut


class UtopianTreeTest(unittest.TestCase):

    def test_input_0_get_1(self):
        num = 0
        result = ut.growth(num)
        self.assertEquals(1, result)

    def test_input_1_get_2(self):
        num = 1
        result = ut.growth(num)
        self.assertEquals(2, result)

    def test_input_3_get_6(self):
        num = 3
        result = ut.growth(num)
        self.assertEquals(6, result)

    def test_input_4_get_7(self):
        num = 4
        result = ut.growth(num)
        self.assertEquals(7, result)
