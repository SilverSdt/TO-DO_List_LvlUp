# <========== import ==========>

from __future__ import annotations

# <========== class ==========>

class Task:
    
    # <----- init ----->
    
    def __init__(self: Task, task_name: str, exp_value: int) -> None:
        self.__name: str = task_name
        self.__exp_value: int = exp_value
        
    # <----- getter ----->
    
    @property
    def name(self: Task) -> str: return self.__name
    
    @property
    def exp_value(self: Task) -> int: return self.__exp_value
    
    # <----- setter ----->
    
    @name.setter
    def name(self: Task, new_name: str) -> None: self.__name = new_name
    
    @exp_value.setter
    def exp_value(self: Task, new_exp_value: int) -> None: self.__exp_value = new_exp_value
    
    # <----- comparateur ----->
    
    def __eq__(self: Task, other: Task | str) -> bool:
        if isinstance(other, Task): return self.__name == other.name
        return self.__name == other
    
    def __ne__(self: Task, other: Task | str) -> bool:
        if isinstance(other, Task): return self.__name != other.name
        return self.__name != other

    
    # <----- str ----->
    
    def __str__(self: Task) -> str: return self.__name
    
    # <----- repr ----->
    
    def __repr__(self: Task) -> str: return self.__name