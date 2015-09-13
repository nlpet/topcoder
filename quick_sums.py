"""
Problem Statement

Given a string of digits, find the minimum number of additions required for the
string to equal some target number. Each addition is the equivalent of
inserting a plus sign somewhere into the string of digits. After all plus signs
are inserted, evaluate the sum as usual. For example, consider the string "12"
(quotes for clarity). With zero additions, we can achieve the number 12.
If we insert one plus sign into the string, we get "1+2", which evaluates to 3.
So, in that case, given "12", a minimum of 1 addition is required to get the
number 3. As another example, consider "303" and a target sum of 6. The best
strategy is not "3+0+3", but "3+03". You can do this because leading zeros do
not change the result.

Write a class QuickSums that contains the method minSums, which takes a String
numbers and an int sum. The method should calculate and return the minimum
number of additions required to create an expression from numbers that
evaluates to sum. If this is impossible, return -1.
"""
import unittest


class TestQuckSums(unittest.TestCase):

    """Unit tests for stock market."""

    def tests(self):
        """Tests."""
        qs = QuickSums()
        self.assertEqual(qs.min_sums("99999", 45), 4)
        self.assertEqual(qs.min_sums("1110", 3), 3)
        self.assertEqual(qs.min_sums("0123456789", 45), 8)
        self.assertEqual(qs.min_sums("99999", 100), -1)
        self.assertEqual(qs.min_sums("382834", 100), 2)


class QuickSums(object):
    def __init__(self):
        pass

    @staticmethod
    def min_sums(string, target):
        r = []
        j = 1
        string = ''.join([c for c in string if c != '0'])
        length = len(string)
        for p in range(0, length):
            pass # TODO




if __name__ == '__main__':
    qs = QuickSums()
    qs.min_sums("382834", 100)
