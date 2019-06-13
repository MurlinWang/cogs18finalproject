"""A collection of function for doing my project."""
import random
import string
import time
from time import sleep
from IPython.display import clear_output



# the class of button that are pressed
class Button():
    
    def __init__(self):
        self.moves = []
    # function that choose random button
    def jump(self, width, length):
        x_coordinate = random.choice(range(width))
        y_coordinate = random.choice(range(length))
        position = [x_coordinate,y_coordinate]
        self.moves.append(position)
        return position

# the class that create a board with buttons 
class buttonBoard():
    
    # the initial state of the number plate
    grid_width = 3
    grid_length = 4
    sleep_time = 0.8
    n_iter = 5
    
    # constructor 
    def __init__(self):
        self.answer = []
        
    # modified from assignment A4 function play_board()
    def board(self, n_iter, sleep_time, button, color):
        
        # take input to increase difficulty of the game
        self.n_iter = n_iter
        self.sleep_time = sleep_time
        """
        Parameters
        ----------
        n_iter : int, optional
            Number of turns to play on the board. default = 1
        sleep_time : float, optional
            Amount of time to pause between turns. default = 0.8.
        button: Botton class, take in the button to jump
        
        color:color class that changes the color of number
        """
        # for each iteratrion
        for it in range(n_iter):

             # Create the grid
            grid_list = [['.'] * self.grid_width for ncols in range(self.grid_length)]
            # initialize numbers
            counter = 0
            for i in range(self.grid_width):
                for j in range(self.grid_width):
                    grid_list[i][j] = str(counter)
                    counter = counter + 1
            grid_list[self.grid_length - 1][0] = '*'
            grid_list[self.grid_length - 1][1] = '9'
            grid_list[self.grid_length - 1][self.grid_width - 1] = '#'
            
             # start pressing buttons
            move_list = button.jump(self.grid_width, self.grid_length)
            self.answer.append(grid_list[move_list[1]][move_list[0]])
            original = str(grid_list[move_list[1]][move_list[0]])
            grid_list[move_list[1]][move_list[0]] = color.RED + original + color.END
            
            # Clear the previous iteration, print the new grid (as a string), and wait
            clear_output(True)
            print('\n'.join(['  '.join(lst) for lst in grid_list]))
            sleep(sleep_time)
            
        return self.answer
    
    # clear the answer from last iteration
    def clean(self):
        self.answer = []
        
    def increase_level():
        new_iter = int(main_board.n_iter + (num_games / 2))
        new_freq = int(main_board.sleep_time - (num_games / 2))
        
    
        
# class that used to change front  
# external code from stack overflow
class color():
    
    BOLD = '\033[1m'
    END = '\033[0m'
    RED = '\033[91m'

#the countdown function for the user to remember
# external code from stack overflow
def count_down(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
