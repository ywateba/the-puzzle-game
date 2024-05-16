from dataclasses import asdict
from pprint import pprint
import unittest

from app.main.python.puzzle.core.numeric_puzzle import (
    NumericPuzzle,
    NumericPuzzleSolver,
)


class TestNumericPuzzle(unittest.TestCase):
    def test_init(self):
        puzzle = NumericPuzzle()
        self.assertEqual(len(puzzle.entries), 6)
        self.assertTrue(1 <= puzzle.target <= 1000)
        self.assertEqual(puzzle.threshold, 0)

    def test_custom_init(self):
        entries = [1, 2, 3, 4, 5]
        target = 15
        threshold = 5
        puzzle = NumericPuzzle(entries, target, threshold)
        self.assertEqual(puzzle.entries, entries)
        self.assertEqual(puzzle.target, target)
        self.assertEqual(puzzle.threshold, threshold)

    def test_puzzle_creation(self):
        # Generate a puzzle
        puzzle_0 = {"entries": [84, 87, 11, 3, 81, 58], "target": 345, "threshold": 10}
        puzzle = NumericPuzzle(**puzzle_0)
        puzzle_asdict = puzzle.as_dict()
        assert puzzle_asdict == puzzle_0
        assert puzzle.entries == puzzle_0["entries"]
        assert puzzle.target == puzzle_0["target"]
        assert puzzle.threshold == puzzle_0["threshold"]


if __name__ == "__main__":
    unittest.main()
