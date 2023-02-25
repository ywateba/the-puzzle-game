from dataclasses import asdict
from pprint import pprint
from puzzle_utils.numeric_puzzle import NumericPuzzleSolver, NumericPuzzle


puzzle_0 = {"entries": [84, 87, 11, 3, 81, 58], "target": 345, "threshold": 10}


def test_puzzle_creation():
    # Generate a puzzle
    puzzle = NumericPuzzle(entries=[84, 87, 11, 3, 81, 58], target=345, threshold=10)

    assert asdict(puzzle) == puzzle_0


def test_solver():
    # Check if the target can be reached using the numbers
    puzzle = NumericPuzzle(**puzzle_0)
    solver = NumericPuzzleSolver(puzzle)
    solver.solve()
    results = solver.get_results()


def test_solution():
    pass
