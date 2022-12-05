def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    max_stack_height = 0

    for line in lines:

        if line[1].isdigit():  # Check if we reach the line where the definition of the stacks ends
            break

        max_stack_height += 1

    # Every crate consists of four characters: '[' + 'X' + '] + ' '
    # +1 because the last space is missing (would also be possible to ceil the result from a regular division)
    stacks_amount = len(lines[max_stack_height]) // 4 + 1

    stacks = [[] for _ in range(stacks_amount)]

    for line in reversed(lines[:max_stack_height]):  # Build the stacks from bottom to top
        for stack in range(stacks_amount+1):
            crate_idx = stack * 4 + 1  # Crates are four characters wide and the contents start at index 1
            if len(line) <= crate_idx:  # When there is no crate in the last stacks, the row ends without extra spaces
                continue
            if line[crate_idx] != " ":
                stacks[stack].append(line[crate_idx])

    stacks2 = [stack_copy[:] for stack_copy in stacks]  # Deep copy for part 2

    for line in lines[max_stack_height+2:]:
        amount = int(line.split()[1])  # Split the move instructions by spaces and take out the relevant numbers
        source = int(line.split()[3]) - 1  # Challenge used 1-based indexing
        destination = int(line.split()[5]) - 1

        # Part 1
        for _ in range(amount):  # To move multiple boxes, we execute the movement several times
            crate = stacks[source].pop()
            stacks[destination].append(crate)

        # Part 2
        stacks2[destination].extend(stacks2[source][-amount:])  # Add the last n boxes
        stacks2[source] = stacks2[source][:-amount]  # Remove last n boxes

    message = ""
    message2 = ""
    for stack in range(stacks_amount):
        message += stacks[stack][-1]
        message2 += stacks2[stack][-1]

    print(f"Part 1: After rearrangement, the crates on top form the message {message}")
    print(f"Part 2: After rearrangement, the crates on top form the message {message2}")


if __name__ == "__main__":
    main()
