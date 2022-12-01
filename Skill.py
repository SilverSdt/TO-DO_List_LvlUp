# <========== import ==========>

from __future__ import annotations
from math import sqrt

from Task import Task

# <========== class ==========>

class Skill:
    
    # <----- init ----->
    
    def __init__(self: Skill, skill_name: str, exp: int = 0, task: list[Task] | None = None) -> None:
        self.__name: str = skill_name
        self.__exp: int = exp
        if task == None: self.__task: list[Task] = []
        else: self.__task: list[Task] = task.copy()
    
    # <----- getter ----->
    
    @property
    def name(self: Skill) -> str: return self.__name
    
    @property
    def exp(self: Skill) -> int: return self.__exp
    
    @property
    def task(self: Skill) -> list[Task]: return self.__task.copy()
    
    @property
    def lvl(self: Skill) -> int: return int((sqrt(self.exp) * 0.57 * 137 + 3 * self.exp * 2.85) / 1000)
    
    # <----- setter ----->
    
    @name.setter
    def name(self: Skill, new_skill_name: str) -> None: self.__name = new_skill_name
    
    @exp.setter
    def exp(self: Skill, new_exp_value: int) -> None: self.__exp = new_exp_value
    
    @task.setter
    def task(self: Skill, new_task: list[Task]) -> None: self.__task = new_task.copy()
    
    # <----- operator ----->
    
    def __iadd__(self: Skill, x: int) -> Skill: return Skill(self.__name, self.__exp + x)
    
    def __add__(self: Skill, x: int) -> Skill: return Skill(self.__name, self.__exp + x)
    
    def __isub__(self: Skill, x: int) -> Skill: return Skill(self.__name, self.__exp - x)
    
    def __sub__(self: Skill, x: int) -> Skill: return Skill(self.__name, self.__exp - x)
    
    # <----- comparator ----->
    
    def __eq__(self: Skill, other_skill: Skill) -> bool: return self.__exp == other_skill.exp
    
    def __ne__(self: Skill, other_skill: Skill) -> bool: return self.__exp != other_skill.exp
    
    def __lt__(self: Skill, other_skill: Skill) -> bool: return self.__exp < other_skill.exp
    
    def __le__(self: Skill, other_skill: Skill) -> bool: return self.__exp <= other_skill.exp
    
    def __gt__(self: Skill, other_skill: Skill) -> bool: return self.__exp > other_skill.exp
    
    def __ge__(self: Skill, other_skill: Skill) -> bool: return self.__exp >= other_skill.exp
    
    # <----- str ----->
    
    def __str__(self: Skill) -> str: return self.__name
    
    # <----- repr ----->
    
    def __repr__(self: Skill) -> str: return self.__name
    
    # <----- task_finished ----->
    
    def task_finished(self: Skill, task: Task | str) -> None:
        if task in self.__task:
            self.__exp += self.__task[self.__task.index(task)].exp_value
            del self.__task[self.__task.index(task)]