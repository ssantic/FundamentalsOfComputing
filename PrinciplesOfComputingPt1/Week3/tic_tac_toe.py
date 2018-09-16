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
    current_player = player
    while board.check_win() is not None:
        empty_squares = board.get_empty_squares()
        (row, col) = random.choice(empty_squares)
        board.move(row, col, current_player)
        current_player = provided.switch_player(current_player)


def mc_update_scores(scores, board, player):
    board_size = board.get_dim()[0]
    winner = board.check_win()
    score_player = (player == winner) * SCORE_CURRENT + (player != winner) * -SCORE_CURRENT
    score_other = (player == winner) * -SCORE_OTHER + (player != winner) * SCORE_OTHER
    for row in range(board_size):
        for col in range(board_size):
            score = (player == board.square(row, col)) * score_player + (provided.switch_player(player) == board.square(row, col)) * score_other
            scores[row][col] += score


def get_best_move(board, scores):
    max_value = max(sum(scores, []))
    potential_moves = []
    for i, row in enumerate(scores):
        for j, score in enumerate(row):
            if score == max_value:
                potential_moves.append((i, j))

    best_move = random.choice(potential_moves)
    return best_move





def mc_move(board, player, trials):
    raise NotImplementedError




# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
