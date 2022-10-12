# run from /git using
# python -m micropython.tests.test_magnetometer -v
import micropython.magnetometer as sm
from micropython.magnetometer import *

def test_script():
    '''
 
    '''


if __name__ == '__main__':
    import doctest
    doctest.testmod(name='test_script', optionflags=doctest.ELLIPSIS)