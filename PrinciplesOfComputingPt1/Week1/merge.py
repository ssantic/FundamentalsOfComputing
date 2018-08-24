"""
Merge function for 2048 game.
"""


def merge(line):
    """
    (line: List[int]) -> List[int]

    Function that merges a single row or column in 2048.
    """

    # Step 1:
    # Iterate over the input and create an output list that has all of the
    # non-zero tiles slid over to the beginning of the list with the
    # appropriate number of zeroes at the end of the list.

    # Step 2:
    # Iterate over the list created in the previous step and create another
    # new list in which pairs of tiles in the first list are replaced with a
    # tile of twice the value and a zero tile.

    # Step 3:
    # Repeat step one using the list created in step two to slide the tiles to
    # the beginning of the list again.
