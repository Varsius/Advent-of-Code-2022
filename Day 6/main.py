def main():
    with open("input.txt", "r") as file:
        line = file.readline()

    for idx in range(0, len(line)-4):

        last_four = line[idx:idx+4]  # Last 4 processed characters

        # If the length of the set of characters is the same --> all characters are different
        if len(last_four) == len(set(last_four)):
            print(f"Part 1: Amount of characters = {idx+4}")
            break

    for idx in range(0, len(line)-14):
        last_fourteen = line[idx:idx+14]
        if len(last_fourteen) == len(set(last_fourteen)):
            print(f"Part 2: Amount of characters = {idx+14}")
            break


if __name__ == "__main__":
    main()
