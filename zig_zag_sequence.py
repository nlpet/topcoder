"""
https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
"""
import unittest


class TestZigZag(unittest.TestCase):

    """Unit tests for stock market."""

    def tests(self):
        """Tests."""
        self.assertEqual(longest_zig_zag_sequence([1, 7, 4, 9, 2, 5]), 6)
        self.assertEqual(longest_zig_zag_sequence([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]), 7)
        self.assertEqual(longest_zig_zag_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2)

def longest_zig_zag_sequence(seq):
    """
    :list : seq
    """
    n = len(seq)
    if n == 1:
        return 1
    deltas = [0 for _ in range(n - 1)]
    for i in range(1, n):
        deltas[i - 1] = seq[i] - seq[i - 1]
    return deltas


if __name__ == '__main__':
    # unittest.main()
    print longest_zig_zag_sequence([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])
