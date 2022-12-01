with open("input.txt", "r") as file:
    lines = file.readlines()

calories = [0]

for line in lines:
    if len(line.strip()) == 0:  # Blank line --> new elf
        calories.append(0)
    else:
        calories[-1] += int(line.strip())  # Add calories to last elf

calories.sort(reverse=True)  # Sort calorie values descending

print(f"Part 1: {max(calories)} are the most calories carried by an elf.")
print(f"Part 2: {sum(calories[:3])} calories are carried by the top three elfs.")


