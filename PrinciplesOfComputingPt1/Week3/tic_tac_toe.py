"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
#import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1           # Number of trials to run
SCORE_CURRENT = 1.0   # Score for squares played by the current player
SCORE_OTHER = 1.0     # Score for squares played by the other player


# Add your functions here.


def mc_trial(board, player):
    raise NotImplementedError


def mc_update_scores(scores, board, player):
    board_size = board.get_dim()[0]
    winner = board.check_win()
    score_player = (player == winner) * SCORE_CURRENT + (player != winner) * -SCORE_CURRENT
    score_other = (player == winner) * -SCORE_OTHER + (player != winner) * SCORE_OTHER
    for row in range(board_size):
        for col in range(board_size):
            score = (winner == board.square(row, col))



def get_best_move(board, scores):
    raise NotImplementedError


def mc_move(board, player, trials):
    raise NotImplementedError




# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
