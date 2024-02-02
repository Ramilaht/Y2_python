import unittest
import datetime
from datetime import date
from weekdays import weekdays, WORKDAY


class TestWeekdays(unittest.TestCase):
    """Implement tests for weekdays here."""
    def test_workday(self):
        test_value1 = weekdays(datetime.datetime(2023, 2, 20), datetime.datetime(2023, 2, 21))
        self.assertEqual(test_value1, 16)
    def test_weekdays_for_full_week(self):

        test_value2 = weekdays(datetime.datetime(2023, 2, 18), datetime.datetime(2023, 2, 25))

        self.assertEqual(test_value2, 40)




if __name__ == "__main__":
    unittest.main()
