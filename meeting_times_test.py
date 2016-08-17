import unittest
from datetime import datetime

from meeting_times import condense_meeting_times, condense_meeting_times_unix_timestamp, iso8601_to_datetime, \
    condense_meeting_times_iso8601, datetime_to_iso8601


class MeetingTimesUnitTest(unittest.TestCase):

    def test_list_of_tuples(self):
        INPUT = [(20, 22), (21, 22), (25, 30)]
        EXPECTED_OUTPUT = [(20, 22), (25, 30)]

        self.assertEqual(condense_meeting_times(INPUT), EXPECTED_OUTPUT)

    def test_list_of_tuples_out_of_order(self):
        INPUT = [(20, 22), (21, 22), (25, 30)]
        INPUT.reverse()
        EXPECTED_OUTPUT = [(20, 22), (25, 30)]

        self.assertEqual(condense_meeting_times(INPUT), EXPECTED_OUTPUT)

    def test_list_of_tuples_out_of_order_2(self):
        INPUT = [(20, 22), (15, 21), (11, 12), (9, 10), (21, 22), (25, 30)]
        INPUT.reverse()
        EXPECTED_OUTPUT = [(9, 10), (11, 12), (15, 22), (25, 30)]

        self.assertEqual(condense_meeting_times(INPUT), EXPECTED_OUTPUT)

    def test_unix_timestamps(self):
        INPUT = [(1447329600, 1447329700), (1447328600, 1447329601), (1447329860, 1447329880)]
        EXPECTED_OUTPUT = [(1447328600, 1447329700), (1447329860, 1447329880)]

        self.assertEqual(condense_meeting_times_unix_timestamp(INPUT), EXPECTED_OUTPUT)

    def test_timestamp_converter(self):
        foo = iso8601_to_datetime('2010-05-08T23:41:54.000Z')
        self.assertIsInstance(foo, datetime)

    def test_datetime_to_iso(self):
        foo = datetime_to_iso8601(datetime(2015, 5, 15))
        self.assertEqual(foo, '2015-05-15T00:00:00.000000Z')

    def test_iso8601(self):
        INPUT = [('2010-05-08T00:41:54.000000Z', '2010-05-08T01:41:54.000000Z'),
                 ('2010-05-08T02:41:54.000000Z', '2010-05-08T05:41:54.000000Z'),
                 ('2010-05-08T01:30:54.000000Z', '2010-05-08T02:00:54.000000Z')]
        EXPECTED_OUTPUT = [('2010-05-08T00:41:54.000000Z', '2010-05-08T02:00:54.000000Z'),
                           ('2010-05-08T02:41:54.000000Z', '2010-05-08T05:41:54.000000Z')]

        self.assertEqual(condense_meeting_times_iso8601(INPUT), EXPECTED_OUTPUT)

if __name__ == '__main__':
    unittest.main()