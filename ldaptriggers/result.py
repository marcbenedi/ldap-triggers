"""
Inspired in https://github.com/dbrattli/OSlash/blob/master/oslash/either.py
and https://github.com/HelmMobile/MultiplatformResult/blob/master/multiplatform-result/src/commonMain/kotlin/cat.helm.result/Result.kt
"""
from typing import TypeVar, Callable

T = TypeVar('T')
R = TypeVar('R')
E = TypeVar('E')

class Result:
    def map(self, _: Callable[[T], R]) -> 'Result':
        return NotImplemented

    @staticmethod
    def of(f: Callable[..., T]) -> 'Result':
        try:
            result = f()
            return Success(result)
        except Exception as e:
            return Failure(e)

class Success(Result):
    def __init__(self, value: T) -> None:
        self._value = value    
        
    def map(self, f: Callable[[T], R]) -> Result:
        return Success(f(self._value))

class Failure(Result):
    def __init__(self, value: E) -> None:
        self._value = value

    def map(self, f: Callable[[T], R]) -> Result:
        return Left(self._value)