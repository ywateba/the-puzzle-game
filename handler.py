import logging
from numeric_puzzle import Operation,NumericPuzzle,NumericPuzzleSolver

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    result = None
    puzzle = NumericPuzzle(**event)
    solver = NumericPuzzleSolver(puzzle)
    solver.solve()
    result = solver.get_results()
    response = {'result': result}
    return response