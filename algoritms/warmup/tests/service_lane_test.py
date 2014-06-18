import unittest
import service_lane as sl


class ServiceLaneTest(unittest.TestCase):
    def setUp(self):
        self.lane = [2, 3, 1, 2, 3, 2, 3, 3]
        self.lane2 = [1, 2, 2, 2, 1]

    def test_input_0_3_get_1(self):
        i, j = 0, 3
        expected_result = 1
        lane = self.lane
        result = sl.get_largest_vehicle_type(lane, i, j)
        self.assertEquals(expected_result, result)

    def test_input_4_6_get_2(self):
        i, j = 4, 6
        expected_result = 2
        lane = self.lane
        result = sl.get_largest_vehicle_type(lane, i, j)
        self.assertEquals(expected_result, result)

    def test_input_6_7_get_3(self):
        i, j = 6, 7
        expected_result = 3
        lane = self.lane
        result = sl.get_largest_vehicle_type(lane, i, j)
        self.assertEquals(expected_result, result)

    def test_lane2_input_2_3_get_2(self):
        i, j = 2, 3
        expected_result = 2
        lane = self.lane2
        result = sl.get_largest_vehicle_type(lane, i, j)
        self.assertEquals(expected_result, result)

    def test_lane2_input_1_4_get_1(self):
        i, j = 1, 4
        expected_result = 1
        lane = self.lane2
        result = sl.get_largest_vehicle_type(lane, i, j)
        self.assertEquals(expected_result, result)
