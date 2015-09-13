"""
Problem statement

Our garden is a square containing plants in n rows and n columns, a total
of n*n plants. The distance between plants within a row is rowDist and
between plants within a column is colDist.

I want to water the garden without getting my shoes muddy. That requires
that I stand outside the garden, never closer than where the next row or
column of the garden would be if it were enlarged. The hose can water plants
that are hoseDist or less away from where I am standing. (Of course, I can
move around and water from various locations.)
Create a class GardenHose that contains the method countDead that takes n,
rowDist, colDist, and hoseDist as inputs and returns the number of plants
that cannot be watered.
"""
import unittest


class TestGardenHose(unittest.TestCase):

    """Unit tests for stock market."""

    def tests(self):
        """Tests."""
        gh = GardenHose()
        self.assertEqual(gh.count_dead(3, 2, 1, 2), 0)
        self.assertEqual(gh.count_dead(3, 2, 1, 1), 3)
        self.assertEqual(gh.count_dead(6, 2, 5, 3), 24)
        self.assertEqual(gh.count_dead(6, 2, 5, 5), 8)


class GardenHose:
    def __init__(self):
        pass

    @staticmethod
    def count_dead(n, row_dist, col_dist, hose_dist):
        count = 0
        for i in range(n):
            for j in range(n):
                if (i + 1) * row_dist <= hose_dist: continue
                if (n - i) * row_dist <= hose_dist: continue

                if (j + 1) * col_dist <= hose_dist: continue
                if (n - j) * col_dist <= hose_dist: continue

                count += 1
        return count

if __name__ == '__main__':
    unittest.main()
