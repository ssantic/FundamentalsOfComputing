"""
Clone of 2048 game
"""

import random
# import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction
# DO NOT MODIFY this dictionary
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    (line: List[int]) -> List[int]

    Function that merges a single row or column in 2048.
    """

    # Step 1:
    # Iterate over the input and create an output list that has all of the
    # non-zero tiles slid over to the beginning of the list with the
    # appropriate number of zeroes at the end of the list.
    intermediate_list = []

    for element in line:
        if element != 0:
            intermediate_list.append(element)

    while len(intermediate_list) < len(line):
        intermediate_list.append(0)

    # Step 2:
    # Iterate over the list created in the previous step and create another
    # new list in which pairs of tiles in the first list are replaced with a
    # tile of twice the value and a zero tile.
    pairs_list = list(intermediate_list)

    prev_val = pairs_list[0]
    for i in range(1, len(pairs_list)):
        current_val = pairs_list[i]
        if current_val == prev_val:
            pairs_list[i - 1] = prev_val * 2
            pairs_list[i] = 0
        prev_val = pairs_list[i]

    # Step 3:
    # Repeat step one using the list created in step two to slide the tiles to
    # the beginning of the list again.
    final_list = []

    for element in pairs_list:
        if element != 0:
            final_list.append(element)

    while len(final_list) < len(pairs_list):
        final_list.append(0)

    return final_list


class TwentyFortyEight:
    """Class to run the game logic"""
    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()

    def reset(self):
        """Reset the game so the grid is empty"""
        self.grid = [[0 for col in range(self.grid_width)]
                     for row in range(self.grid_height)]

        self.new_tile()
        self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty square.
        The tile should be 2 90% of the time and 4 10% of the time.
        """
        zers = []
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                if self.grid[i][j] == 0:
                    zers.append((i, j))

        if len(zers) != 0:
            index = random.choice(zers)
            tile = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
            self.grid[index[0]][index[1]] = tile

    def __str__(self):
        """Return a string representation of the grid for debugging"""
        result = ''
        for irow in range(self.grid_height):
            for icol in range(self.grid_width):
                result += 
            result += '\n'
        result += self.rat_1.__str__()
        result += '\n'
        result += self.rat_2.__str__()

        return result

    def get_grid_height(self):
        """Get the height of the board"""
        return 0

    def get_grid_width(self):
        """Get the width of the board"""
        return 0

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tiles if any tiled moved
        """
        pass

    def set_tile(self, row, col, value):
        """Set tile at postion row, col to have the given value"""
        pass

    def get_tile(self, row, col):
        """Return the value of the tile at position row, col"""
        return 0

# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
