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
