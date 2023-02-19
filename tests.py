

from dataclasses import asdict
from pprint import pprint
from numeric_puzzle import NumericPuzzleSolver,NumericPuzzle


puzzle0 = {'entries': [92, 24, 35, 67, 47, 46], 'target': 373, 'threshold': 100}
puzzle1 ={'entries': [84, 87, 11, 3, 81, 58], 'target': 2000, 'threshold': 10}



# Generate a puzzle
puzzle = NumericPuzzle(**puzzle1)

pprint(asdict(puzzle))


# Check if the target can be reached using the numbers
solver = NumericPuzzleSolver(puzzle)
solver.solve()
pprint(solver.get_results())
#pprint(solver.results)
                          
