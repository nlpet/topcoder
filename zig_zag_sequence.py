"""
https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
"""
import unittest


class TestZigZag(unittest.TestCase):

    """Unit tests for stock market."""

    def tests(self):
        """Tests."""
        self.assertEqual(longest_zig_zag_seq([1, 7, 4, 9, 2, 5]), 6)
        self.assertEqual(longest_zig_zag_seq([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]), 7)
        self.assertEqual(longest_zig_zag_seq([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2)

def longest_zig_zag_seq(seq):
    """
    :list : seq
    """
    n = len(seq)
    best_length = 1
    upwards, downwards = [1], [1]
    for i in range(1, n):
        upwards.append(1)
        downwards.append(1)

        for j in range(i):
            if seq[i] > seq[j]:
                upwards[i] = max(downwards[j] + 1, upwards[i])
            if seq[i] < seq[j]:
                downwards[i] = max(upwards[j] + 1, downwards[i])

        best_length = max(best_length, max(upwards[i], downwards[i]))
    return best_length


if __name__ == '__main__':
    unittest.main()
    # subseq = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    # print subseq
    # print longest_zig_zag_seq(subseq)
