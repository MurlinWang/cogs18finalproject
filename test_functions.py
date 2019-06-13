"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import Button, buttonBoard

##
##

def test_button():
    
    button = Button()
    test = button.jump(4,5)
    isinstance(test, list)
    
def test_buttonBoard():
    
    board = buttonBoard()
    assert board.n_iter == 5
    assert board.sleep_time == 0.8


