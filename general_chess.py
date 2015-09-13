"""
Problem Statement

You have decided that too many people do not know how to play chess. So,
in an effort to teach the rules you must write some software that helps to
understand how chess-pieces affect one another. Your current project involves
the knight and its ability to threaten one or more pieces at once. The knight
has an unusual style of "jumping" around the board. One move consists of
traveling two squares in one of the four cardinal directions, followed by
one square perpendicular to the original direction. For example, if a knight
is on (0,0), it may move to (2,1), (2,-1), (1,2), (1,-2), (-2, 1), (-2,-1),
(-1,2), or (-1,-2). In addition, if a piece is on any of those locations,
it is threatened by the knight on (0,0).

You will be given a String[] pieces, where each element is a comma delimited
set of coordinates. Every element in pieces is formatted as
"<x-coordinate>,<y-coordinate>" (quotes and angle brackets for clarity).

Calculate and return a String[] where each element represents a position
from which a knight threatens every piece in pieces. Your return String[]
must be in the same format as pieces and sorted in increasing order by the
x-coordinate. If two sets of coordinates have the same x-coordinate, the
one with the smaller y-coordinate must come first.
"""
import unittest


class TestGeneralChess(unittest.TestCase):

    """Unit tests for stock market."""

    def tests(self):
        """Tests."""
        gc = GeneralChess()
        self.assertEqual(gc.attack_positions(["0, 0"]), ["-2,-1", "-2,1",
                                                         "-1,-2", "-1,2",
                                                         "1,-2",  "1,2",
                                                         "2,-1",  "2,1"])

        self.assertEqual(gc.attack_positions(["2,1", "-1,-2"]), ["0,0", "1,-1"])


class GeneralChess(object):

    """
    Get knight attack positions that threaten all pieces
    in the given coordinates.
    """

    def __init__(self):
        pass

    @staticmethod
    def get_valid_moves(x, y):
        """
        int: x
        int: y
        """
        return {
            (x - 2, y - 1),
            (x - 2, y + 1),
            (x - 1, y - 2),
            (x - 1, y + 2),
            (x + 1, y - 2),
            (x + 1, y + 2),
            (x + 2, y - 1),
            (x + 2, y + 1)
        }

    def attack_positions(self, pieces):
        """
        list: pieces
        """
        attack_positions = []
        for piece in pieces:
            x, y = map(int, piece.split(','))
            valid_moves = self.get_valid_moves(x, y)
            attack_positions.append(valid_moves)
        attack_positions = set.intersection(*attack_positions)
        return ["%d,%d" % move for move in sorted(attack_positions)]


if __name__ == '__main__':
    unittest.main()
