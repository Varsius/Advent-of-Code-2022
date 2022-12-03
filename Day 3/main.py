def get_priority(item_type: str) -> int:
    """
    Calculates the priority of the given item type
    :param item_type: str (length 1) - item type
    :return: int - priority
    """
    if item_type.isupper():
        return ord(item_type) - 38
    else:
        return ord(item_type) - 96


def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()

    total_priority = 0

    for line in lines:
        # Split line into the two evenly sized compartments
        compartment0 = line[:len(line)//2]
        compartment1 = line[len(line)//2:]

        # Convert compartments to sets of characters and calculate the intersection
        # As stated in the challenge, we can assume there is exactly one common item type
        common_item_type = set(compartment0).intersection(compartment1)

        total_priority += get_priority(common_item_type.pop())

    print(f"Part 1: The sum of properties is {total_priority}")

    total_priority = 0

    for i in range(len(lines) // 3):  # Iterate over triples of lines

        # Calculate intersection like in part 1
        common_item_type = set.intersection(
            set(lines[i*3].strip()),
            set(lines[i*3+1].strip()),
            set(lines[i*3+2].strip())
        )

        total_priority += get_priority(common_item_type.pop())

    print(f"Part 2: The sum of properties is {total_priority}")


if __name__ == "__main__":
    main()
