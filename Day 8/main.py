from math import prod  # Calculates the product of all items in a list


def is_inbound(x: int, y: int, grid: list[list[int]]) -> bool:
    """
    Checks whether the given coordinates are valid with respect to the given grid
    :param x: x-coordinate
    :param y: y-coordinate
    :param grid: grid
    :return: Is valid
    """
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def check_tree(x: int, y: int, grid: list[list[int]]) -> (bool, int):
    """
    Checks if the tree is visible and calculates the scenic score.
    Combines both task of part 1 and 2 because they are similar solution wise.
    :param x: x-coordinate
    :param y: y-coordinate
    :param grid: grid
    :return: is visible & scenic score
    """

    visible = False
    viewing_distances = [1, 1, 1, 1]  # You can see at least one tree in each direction

    directions = [
        [1, 0],   # +x == right
        [0, 1],   # +y == down
        [-1, 0],  # -x == left
        [0, -1]   # -y == up
    ]

    for idx, direction in enumerate(directions):  # Traverse the grid in each direction
        x1, y1 = x + direction[0], y + direction[1]
        while is_inbound(x1, y1, grid):  # Check if we are still on the grid

            # Check if other tree is bigger or equal --> not visible from this direction
            # break does not trigger else statement below (only a false while condition does == out of bound)
            if grid[y1][x1] >= grid[y][x]:
                break

            x1 += direction[0]  # Do another step in the direction
            y1 += direction[1]
            viewing_distances[idx] += 1

        else:
            viewing_distances[idx] -= 1  # If we stepped out of bound than we do not see another tree from there
            visible = True  # We did not find a tree that was large enough --> given tree is visible

    return visible, prod(viewing_distances)


def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()

    grid = []

    for line in lines:
        row = [int(tree) for tree in line.strip()]
        grid.append(row)

    amount_visible = 0
    best_scenic_score = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            is_visible, scenic_score = check_tree(x, y, grid)
            amount_visible += is_visible
            best_scenic_score = max(scenic_score, best_scenic_score)

    print(f"Part 1: Amount of trees visible = {amount_visible}")
    print(f"Part 2: Highest scenic score = {best_scenic_score}")


if __name__ == "__main__":
    main()
