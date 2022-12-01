# <========== Import ==========>
import sys, os

parentdir = os.path.realpath(os.path.join(os.path.dirname(__file__),os.pardir))
if parentdir not in sys.path:
    sys.path.insert(1, parentdir)
    
from Task import Task
    
# <========== Tests ==========>

def test_init_getter() -> None:
    """ test de l'init et des getter
    
    >>> new_task : Task = Task('new_task', 100)
    
    >>> new_task.name
    'new_task'
    
    >>> new_task.exp_value
    100
    """
    return None

def test_setter() -> None:
    """ test des setter
    
    >>> new_task : Task = Task('new_task', 100)
    
    >>> new_task.name = 'new_name'
    >>> new_task.name
    'new_name'
    
    >>> new_task.exp_value = 200
    >>> new_task.exp_value
    200
    """
    return None
    
def test_comparateur() -> None:
    """ test des comparateurs
    
    >>> new_task_1 : Task = Task('new_task', 100)
    >>> new_task_2 : Task = Task('new_task', 100)
    >>> new_task_3 : Task = Task('new_task_3', 100)
    
    
    >>> new_task_1.__eq__(new_task_2)
    True
    
    >>> new_task_1.__eq__(new_task_3)
    False

    >>> new_task_1.__ne__(new_task_2)
    False

    >>> new_task_1.__ne__(new_task_3)
    True
    """
    return None
    
def test_str_repr() -> None:
    """ test du str et repr
    
    >>> new_task: Task = Task('new_task', 100)
    
    >>> new_task.__str__()
    'new_task'
    
    >>> new_task.__repr__()
    'new_task'
    """
    return None

# <========== main ==========>

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)