import unittest
from utils import convert_date

class ConvertDateTests(unittest.TestCase):
    """
    Testing the convert_date function
    """
    def test_convert_date_with_day_time(self):
        """
        Test if a date with day and time is converted correctly
        """
        test_date = "2021-10-03T12:00:00Z"
        expected_date = "03 Oct 2021, 12:00"
        self.assertEqual(convert_date(test_date), expected_date)

    def test_convert_date_with_day_only(self):
        """
        Test if a date with only a day is converted correctly
        """
        test_date = "2021-10-03"
        expected_date = "03 Oct 2021"
        self.assertEqual(convert_date(test_date), expected_date)

    def test_convert_date_with_wrong_format(self):
        """
        Test if a date with a wrong format raises a ValueError
        """
        test_date = "2021-10-03T12:00:00"
        with self.assertRaises(ValueError):
            convert_date(test_date)

    def test_convert_date_with_none_value(self):
        """
        Test if a None value raises a ValueError
        """
        test_date = None
        with self.assertRaises(TypeError):
            convert_date(test_date)

    def test_convert_date_with_wrong_type(self):
        """
        Test if a wrong type raises a ValueError
        """
        test_date = 123
        with self.assertRaises(TypeError):
            convert_date(test_date)
    
    def test_convert_date_with_leap_year(self):
        """
        Test if 29th February of a leap year is converted correctly
        """
        test_date = "2020-02-29"
        expected_date = "29 Feb 2020"
        self.assertEqual(convert_date(test_date), expected_date)

    def test_convert_date_with_lowest_date(self):
        """
        Test if the lowest possible date is converted correctly
        """
        test_date = "0001-01-01"
        expected_date = "01 Jan 0001"
        self.assertEqual(convert_date(test_date), expected_date)

    def test_convert_date_with_highest_date(self):
        """
        Test if the highest possible date is converted correctly
        """
        test_date = "9999-12-31"
        expected_date = "31 Dec 9999"
        self.assertEqual(convert_date(test_date), expected_date)

if __name__ == '__main__':
    unittest.main()
