# https://www.hackerrank.com/challenges/triplets

import unittest
import triplets


class Triplets(unittest.TestCase):
    def test_case_sample0(self):
        l = [1, 2, 3]
        expected = 1
        result = triplets.count_triples(l)
        self.assertEqual(expected, result)

    def test_case_sample1(self):
        l = [1, 1, 2, 2, 3, 4]
        expected = 4
        result = triplets.count_triples(l)
        self.assertEqual(expected, result)

    def test_case_sample2(self):
        l = [2, 2, 2]
        expected = 0
        result = triplets.count_triples(l)
        self.assertEqual(expected, result)

    def test_case_sample3(self):
        l = [3, 2, 1]
        expected = 0
        result = triplets.count_triples(l)
        self.assertEqual(expected, result)

    def test_case_sample4(self):
        l = [1, 1, 5, 4, 3, 6, 6, 5, 9, 10]
        expected = 28
        result = triplets.count_triples(l)
        self.assertEqual(expected, result)

    def test_case_3(self):
        l = [539, 247, 385, 496, 885, 623, 420, 144, 968, 735, 915, 625, 534,
             42, 11, 679, 152, 244, 295, 818, 396, 692, 815, 991, 33, 669, 397,
             553, 547, 825, 210, 662, 211, 808, 377, 761, 625, 335, 868, 995,
             776, 767, 439, 874, 331, 556, 301, 872, 560, 94, 984, 755, 789,
             407, 15, 193, 769, 680, 455, 855, 506, 963, 502, 676, 108,
             249, 331, 844, 638, 808, 997, 651, 849, 203, 731, 531, 14, 419,
             775, 9, 180, 929, 223, 54, 260, 737, 545, 317, 525, 200, 256, 564,
             597, 648, 704, 550, 150, 976, 412, 554, 797, 504, 381, 748, 65,
             378, 699, 209, 129, 553, 483, 447, 607, 773, 322, 305, 176, 53,
             224, 630, 366, 400, 444, 370, 285, 16, 898, 155, 133, 557, 576,
             178, 266, 357, 711, 878, 614, 819, 737, 133, 591, 720, 762, 633,
             197, 31, 588, 589, 873, 877, 304, 358, 200, 254, 960, 915, 947,
             480, 730, 955, 546, 107, 238, 0, 926, 35, 857, 113, 114, 593,
             360, 354, 418, 357, 585, 729, 15, 563, 102, 917, 643, 419, 967,
             747, 269, 395, 303, 473, 103, 748, 385, 658, 459, 406, 930, 824,
             132, 973, 603, 897, 920, 950, 231, 480, 203, 900, 520, 533, 258,
             3, 676, 950, 934, 780, 879, 832, 574, 549, 542, 249, 771, 310]
        expected = 271944
        result = triplets.count_triples(l)
        self.assertEqual(expected, result)
