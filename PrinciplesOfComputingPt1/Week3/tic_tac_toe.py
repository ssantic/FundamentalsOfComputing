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
    """Take an initial board and iteratively play the game until over"""
    current_player = player
    while board.check_win() is None:
        empty_squares = board.get_empty_squares()
        (row, col) = random.choice(empty_squares)
        board.move(row, col, current_player)
        current_player = provided.switch_player(current_player)


def mc_update_scores(scores, board, player):
    """Take a grid of scores, score the completed board, and update the grid"""
    board_size = board.get_dim()
    winner = board.check_win()
    score_player = (player == winner) * SCORE_CURRENT + (provided.switch_player(player) == winner) * -SCORE_CURRENT
    score_other = (player == winner) * -SCORE_OTHER + (provided.switch_player(player) == winner) * SCORE_OTHER
    for row in range(board_size):
        for col in range(board_size):
            score = (player == board.square(row, col)) * score_player + (provided.switch_player(player) == board.square(row, col)) * score_other
            scores[row][col] += score


def get_best_move(board, scores):
    """Find all of the empty squares with the maximum score and return one"""
    empty_squares = board.get_empty_squares()
    empty_scores = []
    for (row, col) in empty_squares:
        empty_scores.append(scores[row][col])
    max_score = max(empty_scores)
    potential_moves = []
    for (row, col) in empty_squares:
        if scores[row][col] == max_score:
            potential_moves.append((row, col))

    best_move = random.choice(potential_moves)
    return best_move


def mc_move(board, player, trials):
    """Return a board move for a machine player"""
    board_size = board.get_dim()
    scores = [[0 for _ in range(board_size)] for _ in range(board_size)]
    for dummy_trial in range(trials):
        trial_board = board.clone()
        mc_trial(trial_board, player)
        mc_update_scores(scores, trial_board, player)
    best_move = get_best_move(board, scores)
    return best_move






# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
