# https://www.hackerrank.com/challenges/flowers

import unittest
import flowers


class FlowersTest(unittest.TestCase):
    def test_case1_get_13(self):
        n, k = [3, 3]
        flowers_cost = [2, 5, 6]
        expected_result = 13
        result = flowers.buy_flowers(n, k, flowers_cost)
        self.assertEqual(expected_result, result)

    def test_case2_get_163578911(self):
        n, k = [50, 3]
        flowers_cost = [390225, 426456, 688267, 800389, 990107, 439248, 240638,
                        15991, 874479, 568754, 729927, 980985, 132244, 488186,
                        5037, 721765, 251885, 28458, 23710, 281490, 30935,
                        897665, 768945, 337228, 533277, 959855, 927447, 941485,
                        24242, 684459, 312855, 716170, 512600, 608266, 779912,
                        950103, 211756, 665028, 642996, 262173, 789020, 932421,
                        390745, 433434, 350262, 463568, 668809, 305781, 815771,
                        550800]
        expected_result = 163578911
        result = flowers.buy_flowers(n, k, flowers_cost)
        self.assertEqual(expected_result, result)
