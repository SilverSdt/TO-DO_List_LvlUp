# <========== Import ==========>
import sys, os

parentdir = os.path.realpath(os.path.join(os.path.dirname(__file__),os.pardir))
if parentdir not in sys.path:
    sys.path.insert(1, parentdir)
    
from Skill import Skill
from Task import Task
    
# <========== Tests ==========>

def test_init_getter() -> None:
    """ Test de l'init et des getter
    
    >>> new_skill: Skill = Skill('new skill')
    
    >>> new_skill.name
    'new skill'
    
    >>> new_skill.exp
    0
    
    >>> new_skill.lvl
    0
    
    >>> new_skill.task
    []
    
    >>> new_skill: Skill = Skill('new skill', 100, [Task('new_task', 100)])
    
    >>> new_skill.exp
    100
    
    >>> new_skill.lvl
    1
    
    >>> new_skill.task
    [new_task]
    """
    return None

def test_setter() -> None:
    """  Test des setter
    
    >>> new_skill: Skill = Skill('new skill')
    
    >>> new_skill.name = 'new name'
    >>> new_skill.name
    'new name'
    
    >>> new_skill.exp = 100
    >>> new_skill.exp
    100
    
    >>> new_skill.task = [Task('new_task', 100)]
    >>> new_skill.task
    [new_task]
    """
    return None

def test_operator() -> None:
    """ Test des operateurs
    
    >>> new_skill: Skill = Skill('new skill')
    >>> new_skill = new_skill + 10
    >>> new_skill.exp
    10
    
    >>> new_skill: Skill = Skill('new skill', 10)
    >>> new_skill = new_skill - 10
    >>> new_skill.exp
    0
    
    >>> new_skill: Skill = Skill('new skill')
    >>> new_skill += 10
    >>> new_skill.exp
    10
    
    >>> new_skill: Skill = Skill('new skill', 10)
    >>> new_skill -= 10
    >>> new_skill.exp
    0
    """
    return None

def test_comparator() -> None:
    """ Test des comparateurs
    
     
    >>> new_skill_1: Skill = Skill('new skill 1')
    >>> new_skill_2: Skill = Skill('new skill 2')
    
    >>> new_skill_1 == new_skill_2
    True
    
    >>> new_skill_1 != new_skill_2
    False
    
    >>> new_skill_1 < new_skill_2
    False
    
    >>> new_skill_1 > new_skill_2
    False
    
    >>> new_skill_1 <= new_skill_2
    True
    
    >>> new_skill_1 >= new_skill_2
    True
    
    
    >>> new_skill_1: Skill = Skill('new skill 1')
    >>> new_skill_2: Skill = Skill('new skill 2', 10)
    
    
    >>> new_skill_1 == new_skill_2
    False
    
    >>> new_skill_1 != new_skill_2
    True
    
    >>> new_skill_2 < new_skill_1
    False
    
    >>> new_skill_1 < new_skill_2
    True
    
    >>> new_skill_2 > new_skill_1
    True
    
    >>> new_skill_1 > new_skill_2
    False
    
    >>> new_skill_2 <= new_skill_1
    False
    
    >>> new_skill_1 <= new_skill_2
    True
    
    >>> new_skill_2 >= new_skill_1
    True
    
    >>> new_skill_1 >= new_skill_2
    False
    """
    return None

def test_str_repr() -> None:
    """ test du str et repr
    
    >>> new_skill: Skill = Skill('new skill')
    
    >>> new_skill.__str__()
    'new skill'
    
    >>> new_skill.__repr__()
    'new skill'
    """
    return None

def test__task_finished() -> None:
    """
    >>> new_skill: Skill = Skill('new skill', 100, [Task('new_task', 100)])
    >>> new_skill.task_finished('new_task')
    
    >>> new_skill.task
    []
    
    >>> new_skill.exp
    200
    
    """
    return None

# <========== main ==========>

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)