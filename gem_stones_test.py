# https://www.hackerrank.com/challenges/gem-stones

import unittest
import gem_stones as gs


class GemStonesTest(unittest.TestCase):
    def test_input_sample_case_get_2(self):
        rocks = ["abcdde", "baccd", "eeabg"]
        expected_result = 2
        result = gs.get_number_of_gem_elements(rocks)
        self.assertEquals(expected_result, result)
