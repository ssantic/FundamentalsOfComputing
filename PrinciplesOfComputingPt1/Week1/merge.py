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
    pairs_list = []

    for i in range(len(intermediate_list), 2):
        pairs_list.append(intermediate_list[i * 2])
        pairs_list.list_append(0)

    # Step 3:
    # Repeat step one using the list created in step two to slide the tiles to
    # the beginning of the list again.
