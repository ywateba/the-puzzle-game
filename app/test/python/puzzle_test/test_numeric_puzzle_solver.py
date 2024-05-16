import unittest
from app.main.python.puzzle.core.numeric_puzzle import (
    NumericPuzzle,
    NumericPuzzleSolution,
    NumericPuzzleSolver,
)


class TestNumericPuzzleSolver(unittest.TestCase):
    def test_solve_simple(self):
        puzzle = NumericPuzzle([2, 3, 5], 10)
        solver = NumericPuzzleSolver(puzzle)
        solver.solve()
        self.assertEqual(len(solver.puzzle.solutions), 2)
        self.assertEqual(solver.puzzle.solutions[0].result, 10)

    def test_solve_multiple(self):
        puzzle = NumericPuzzle([2, 3, 5, 7], 17)
        solver = NumericPuzzleSolver(puzzle)
        solver.solve()
        self.assertEqual(len(solver.puzzle.solutions), 2)
        # self.assertIn(
        #     NumericPuzzleSolution(17, ["7 + 5 + 2 + 3"]), solver.puzzle.solutions
        # )
        # self.assertIn(
        #     NumericPuzzleSolution(17, ["7 + 3 + 2 + 5"]), solver.puzzle.solutions
        # )

    def test_solve_no_solution(self):
        puzzle = NumericPuzzle([2, 3, 5], 12)
        solver = NumericPuzzleSolver(puzzle)
        solver.solve()
        self.assertEqual(len(solver.puzzle.solutions), 0)

    def test_solve_with_threshold(self):
        puzzle = NumericPuzzle([2, 3, 5], 12, threshold=2)
        solver = NumericPuzzleSolver(puzzle)
        solver.solve()
        self.assertEqual(len(solver.puzzle.solutions), 3)

    def test_solve_with_large_numbers(self):
        puzzle = NumericPuzzle([100, 200, 300], 600)
        solver = NumericPuzzleSolver(puzzle)
        solver.solve()
        self.assertEqual(len(solver.puzzle.solutions), 2)

    def test_solver(self):
        # Check if the target can be reached using the numbers
        puzzle_0 = {"entries": [84, 87, 11, 3, 81, 58], "target": 345, "threshold": 10}
        puzzle = NumericPuzzle(**puzzle_0)
        solver = NumericPuzzleSolver(puzzle)
        solver.solve()

        assert len(puzzle.solutions) > 0


if __name__ == "__main__":
    unittest.main()
