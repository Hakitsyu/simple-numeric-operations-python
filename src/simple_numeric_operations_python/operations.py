from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def execute(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class Number(Operation):
    def __init__(self, value: float):
        self.__value = value

    def execute(self) -> float:
        return self.__value
    
    def __str__(self) -> str:
        return str(self.__value)
    
class Sum(Operation):
    def __init__(self, left: Operation, right: Operation):
        self.__left = left
        self.__right = right

    def execute(self) -> float:
        return self.__left.execute() + self.__right.execute()

    def __str__(self) -> str:
        return f"({self.__left} + {self.__right})"
    
class Subtract(Operation):
    def __init__(self, left: Operation, right: Operation):
        self.__left = left
        self.__right = right

    def execute(self) -> float:
        return self.__left.execute() - self.__right.execute()
    
    def __str__(self) -> str:
        return f"({self.__left} - {self.__right})"
    
class Multiply(Operation):
    def __init__(self, left: Operation, right: Operation):
        self.__left = left
        self.__right = right

    def execute(self) -> float:
        return self.__left.execute() * self.__right.execute()
    
    def __str__(self) -> str:
        return f"({self.__left} * {self.__right})"
    
class Divide(Operation):
    def __init__(self, left: Operation, right: Operation):
        self.__left = left
        self.__right = right

    def execute(self) -> float:
        return self.__left.execute() / self.__right.execute()
    
    def __str__(self) -> str:
        return f"({self.__left} / {self.__right})"