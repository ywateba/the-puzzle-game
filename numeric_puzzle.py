from typing import List
from dataclasses import dataclass
from random import randint


class Operation:
    name: str 
    args: List[int]

    @classmethod
    def addition(cls,a , b):
        return a+b , f"{a} + {b} = {a+b}"

    @classmethod
    def substraction(cls,a , b):
        return max(a,b) - min(a,b) ,f"{max(a,b)} - {min(a,b)} = {max(a,b) - min(a,b)}"

    @classmethod
    def multiplication(cls,a , b):
        return a*b , f"{a} x {b} = {a*b}"

    @classmethod
    def division(cls,a , b):
        if a == 0 or b == 0:
            return -1 ,"Invalid"

        if max(a,b) % min(a,b) == 0:
            return int(max(a,b) / min(a,b)) ,f"{max(a,b)} / {min(a,b)} = {int(max(a,b) / min(a,b))}"
        
        return -1, "Invalid"

    @classmethod
    def operations(cls):
        arithmetic_operations = [
            cls.addition,
            cls.substraction,
            cls.multiplication,
            cls.division
        ]
        return arithmetic_operations

@dataclass
class NumericPuzzleSolution:
    result: int
    operations: List[str]

@dataclass
class NumericPuzzle:
    entries: List[int]
    target: int 
    threshold: int 


    def __init__(self) -> None:
        entries = [randint(1, 100) for i in range(6)]
        target = randint(1, 1000)

    def __init__(self, entries:List[int] = None,target:int=None, threshold= None):
        self.entries = entries if entries else [randint(1, 100) for i in range(6)]
        self.target = target if target else randint(1, 1000)
        self.threshold = threshold if threshold else 10

class NumericPuzzleSolver:
    
    def __init__(self, puzzle: NumericPuzzle) -> None:
        self.puzzle = puzzle
        self.threshold = puzzle.threshold
        self.results = [] 

    def __choices(self,numbers, i):
        return [numbers[k] for k in range(i,len(numbers)) if k!=i]

    def __is_close(self,result):
        if abs(self.puzzle.target- result) <= self.threshold:
            return True
        
        return False
    
    def __valid_results(self):
        return[result for result in self.results if result["result"]==self.puzzle.target]
        
    def __closest_results(self):
        best_results = []
        min_reached = 100
        for result in self.results:
            reached = abs(self.puzzle.target - result['result'])
            if reached == min_reached:
                best_results.append(result)
            elif reached < min_reached:
                min_reached = reached
                best_results.clear()
                best_results.append(result)

        return best_results

    def __reach_target(self,entries,path):
        if len(entries) == 1:
            result = entries[0]
            if self.__is_close(result):
                self.results.append(
                    {
                        "result": entries[0],
                        "operations": path
                    }
                )
        else:
            for i in range(len(entries)):
                a = entries[i]
                current_choices = self.__choices(entries, i)
                for j in range(len(current_choices)):
                    b = current_choices[j]
                    for operation in Operation.operations():
                        result,op_name = operation(a,b)
                        if result >= 0:
                            if result == self.puzzle.target:
                                path.append(op_name)
                                self.results.append({
                                    "result": result,
                                    "operations": path
                                }) 
                            else:
                                next_choices = self.__choices(current_choices,j)
                                next_path = [op for op in path]

                                next_choices.append(result)
                                next_path.append(op_name)
                                self.__reach_target(next_choices,next_path)
                            
    def solve(self):
        self.__reach_target(self.puzzle.entries, [])

    def get_results(self):
        valids = self.__valid_results()
        if len(valids):
            return valids

        return self.__closest_results()



    
        
        
 