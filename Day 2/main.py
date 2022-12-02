"""
Contains the score gained for every combination of shapes.
Row == Shape opponent chose
Column == Shape we chose
"""
match_result_scores = [  # X A B C
    [3, 6, 0],           # A
    [0, 3, 6],           # B
    [6, 0, 3]            # C
]

"""
Contains the shape we have to choose to get the desired result.
Row == Shape opponent chose
Column == Desired result
"""
shapes_to_choose = [  # X Loose Draw Win
    ['C', 'A', 'B'],  # A
    ['A', 'B', 'C'],  # B
    ['B', 'C', 'A']   # C
]


def get_shape_score(shape: str) -> int:
    """
    Calculates the score you get when choosing the given shape.
    :param shape: str - Encoded shape
    :return: int - score
    """

    # ord('A') == 65 --> If we subtract 64 from the ASCII values we get the score
    return ord(shape) - 64


def get_match_result_score(opponent_shape: str, my_shape: str) -> int:
    """
    Calculates the score you get for the chosen shapes.
    :param opponent_shape: str - Encoded shape
    :param my_shape: str - Encoded shape
    :return: int - score
    """

    return match_result_scores[ord(opponent_shape) - 65][ord(my_shape) - 65]


def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()

    score = 0
    score2 = 0

    for line in lines:

        opponent_shape, strategy = line.split()

        # Part 1: Shift the strategy by 23 letters backwards in the alphabet
        my_shape = chr(ord(strategy) - 23)

        score += get_shape_score(my_shape)

        score += get_match_result_score(opponent_shape, my_shape)

        # Part 2: The ASCII value of 'X' is 88 --> Subtract to get the desired result
        my_shape = shapes_to_choose[ord(opponent_shape) - 65][ord(strategy)-88]

        score2 += get_shape_score(my_shape)

        score2 += get_match_result_score(opponent_shape, my_shape)

    print(f"Part 1: Our total score is {score}.")
    print(f"Part 2: Our total score is {score2}")


if __name__ == "__main__":
    main()
