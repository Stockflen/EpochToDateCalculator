import unittest
import random
import datetime
from task import find_date_time


class TestCase(unittest.TestCase):    

    def test0(self):
        input_num = 0
        expected = "01-01-1970"
        self.assertEqual(find_date_time(input_num), expected)

    def test1(self):
        input_num = 123456789
        expected = "11-29-1973"
        self.assertEqual(find_date_time(input_num), expected)

    def test2(self):
        input_num = 2697993
        expected = "02-01-1970"
        self.assertEqual(find_date_time(input_num), expected)

    def test3(self):
        input_num = 201653971200
        expected = "02-29-8360"
        self.assertEqual(find_date_time(input_num), expected)

    def test4(self):
        input_num = 1586000460
        expected = '04-04-2020'
        self.assertEqual(find_date_time(input_num), expected)

    def test5(self):
        input_num = 1579952460
        expected = '01-25-2020'
        self.assertEqual(find_date_time(input_num), expected)

    def test6(self):
        input_num = 169516799
        expected = '05-16-1975'
        self.assertEqual(find_date_time(input_num), expected)

    def test7(self):
        input_num = 1517852771
        expected = '02-05-2018'
        self.assertEqual(find_date_time(input_num), expected)

    def test8(self):
        for i in range(0, 1500):
            val = random.randint(0, 2534006682)
            expected = datetime.datetime.utcfromtimestamp(val).strftime("%m-%d-%Y")
            self.assertEqual(find_date_time(val), expected)

    def test9(self):
        val = 0
        for i in range(0, 365):
            val += 86400
            expected = datetime.datetime.utcfromtimestamp(val).strftime("%m-%d-%Y")
            self.assertEqual(find_date_time(val), expected)

    def test10(self):
        val = 978265001
        expected = '12-31-2000'
        self.assertEqual(find_date_time(val), expected)

    def test11(self):
        val = 725792492
        expected = '12-31-1992'
        self.assertEqual(find_date_time(val), expected)


if __name__ == '__main__':
    unittest.main()