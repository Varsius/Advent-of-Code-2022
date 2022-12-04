def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    amount_fully_contained = 0
    amount_overlapped = 0

    for line in lines:
        assignments0, assignments1 = line.split(",")

        # IDs need to be converted to int because otherwise the comparisons will fail
        # for cases like '10' < '2' == True
        assignments0_start, assignments0_end = [int(ID) for ID in assignments0.split("-")]
        assignments1_start, assignments1_end = [int(ID) for ID in assignments1.split("-")]

        # Check if the ranges are fully contained in each other
        if (assignments0_start >= assignments1_start and assignments0_end <= assignments1_end) or \
                (assignments1_start >= assignments0_start and assignments1_end <= assignments0_end):
            amount_fully_contained += 1

        # Ranges overlap if the end of either range is contained in the other
        if (assignments1_start <= assignments0_end <= assignments1_end) or \
                (assignments0_start <= assignments1_end <= assignments0_end):
            amount_overlapped += 1

    print(f"Part 1: In {amount_fully_contained} assignment pairs one range fully contains the other.")
    print(f"Part 2: In {amount_overlapped} assignment pairs do the ranges overlap.")


if __name__ == "__main__":
    main()
