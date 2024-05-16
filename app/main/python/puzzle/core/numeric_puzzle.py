from typing import List
from dataclasses import dataclass, field
from random import randint
from puzzle.utils.base_dictable import BaseDictable


class Operation:
    name: str
    args: List[int]

    @classmethod
    def addition(cls, a, b):
        """
        Returns the sum of the two positive integers and the string representation of the operation
        :param a: First number
        :param b: Second number
        :return: sum, always positive
        """
        return a + b, f"{a} + {b} = {a+b}"

    @classmethod
    def substraction(cls, a, b):
        """
        Returns the difference between the two positive integers and the string representation of the operation
        :param a: First number
        :param b: Second number
        :return: difference, always positive or null
        """
        return max(a, b) - min(a, b), f"{max(a,b)} - {min(a,b)} = {max(a,b) - min(a,b)}"

    @classmethod
    def multiplication(cls, a, b):
        """
        Returns the product of the two positive integers and the string representation of the operation
        :param a: First number
        :param b: Second number
        :return: product

        """
        return a * b, f"{a} x {b} = {a*b}"

    @classmethod
    def division(cls, a, b):
        """
        Returns the quotient of the two positive integers and the string representation of the operation
        :param a: First number
        :param b: Second number
        :return: quotient, always positive or null
        """
        if a == 0 or b == 0:
            return -1, "Invalid"

        if max(a, b) % min(a, b) == 0:
            return (
                int(max(a, b) / min(a, b)),
                f"{max(a,b)} / {min(a,b)} = {int(max(a,b) / min(a,b))}",
            )

        return -1, "Invalid"

    @classmethod
    def operations(cls):
        """
        Returns a list of operations
        :return: list of operations
        """
        arithmetic_operations = [
            cls.addition,
            cls.substraction,
            cls.multiplication,
            cls.division,
        ]
        return arithmetic_operations


@dataclass
class NumericPuzzleSolution(BaseDictable):
    result: int
    operations: List[str]


@dataclass
class NumericPuzzle(BaseDictable):
    entries: List[int]
    target: int
    threshold: int
    solutions: List[NumericPuzzleSolution] = None

    def __init__(self, entries: List[int] = None, target: int = None, threshold=None):
        self.entries = entries if entries else [randint(1, 100) for i in range(6)]
        self.target = target if target else randint(1, 1000)
        self.threshold = threshold if threshold else 0


class NumericPuzzleSolver:
    def __init__(self, puzzle: NumericPuzzle) -> None:
        self.puzzle = puzzle
        self.solutions = []

    def __choices(self, numbers, i):
        return [numbers[k] for k in range(i, len(numbers)) if k != i]

    def __is_close(self, result, threshold=1e-6):
        return abs(self.puzzle.target - result) <= self.puzzle.threshold

    def __valid_solutions(self):
        return [
            solution
            for solution in self.solutions
            if self.__is_close(solution.result, self.puzzle.threshold)
        ]

    def __closest_solutions(self):
        best_solutions = []
        min_reached = 100
        for solution in self.solutions:
            reached = abs(self.puzzle.target - solution.result)
            best_solutions.append(solution)
            if reached <= min_reached:
                min_reached = reached
                best_solutions.clear()
                best_solutions.append(solution)

        return best_solutions

    def __reach_target(self, entries, path):
        if len(entries) == 1:
            result = entries[0]
            if self.__is_close(result):
                solution = NumericPuzzleSolution(entries, path)
                self.solutions.append(solution)
        else:
            for i, a in enumerate(entries):
                current_choices = self.__choices(entries, i)
                for b in current_choices:
                    for operation in Operation.operations():
                        try:
                            result, op_name = operation(a, b)
                            if result >= 0:
                                if self.__is_close(result):
                                    solution = NumericPuzzleSolution(
                                        result, path + [op_name]
                                    )
                                    print(solution)
                                    self.solutions.append(solution)
                                else:
                                    next_choices = self.__choices(
                                        current_choices, current_choices.index(b)
                                    )
                                    self.__reach_target(
                                        next_choices + [result], path + [op_name]
                                    )
                        except Exception as e:
                            # Handle any exceptions that may occur during the operation
                            print(f"An error occurred: {e}")
                            # Add additional error handling logic as needed

    def solve(self):
        self.__reach_target(self.puzzle.entries, [])
        self.puzzle.solutions = self.__get_solutions()

    def __get_solutions(self):
        valids = self.__valid_solutions()
        if len(valids):
            return valids

        return self.__closest_solutions()
