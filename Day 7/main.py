def calculate_directory_size(directory: str, directories: dict, directory_sizes: dict):
    """
    Calculates the total size of the given directory
    :param directory: Path of the directory
    :param directories: Contains the content of each directory
    :param directory_sizes: Contains the size if each directory
    :return: total size
    """

    size = 0

    for content in directories[directory]:
        if content.isnumeric():  # Files
            size += int(content)
        else:
            size += directory_sizes[content]  # Other directories

    return size


def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()

    directory_log = ["/"]  # Keeps track of where we are in the directory tree
    directories = {}  # Contents of each directory
    directory_levels = {"/": 1}  # Keeps track how deep each directory is located in the directory tree
    directory_sizes = {}  # Sizes of the directories

    for line in lines:

        if line.startswith("$ cd"):
            destination = line.split()[2]

            if destination == "/":
                directory_log = ["/"]
                continue

            if destination == "..":
                directory_log.pop()
                continue

            directory_log.append(destination)
            # Since the names of the directories are not unique we have to use the full path as a key
            directory_levels["/".join(directory_log)] = len(directory_log)  # Save how many directories we have gone up
            continue

        if line.startswith("dir"):
            directory_name = line.split()[1]
            directory_path = "/".join(directory_log)
            if directory_path in directories:
                directories[directory_path].append("/".join(directory_log + [directory_name]))
            else:
                directories[directory_path] = ["/".join(directory_log + [directory_name])]
            continue

        if line.startswith("$ ls"):
            continue

        file_size = line.split()[0]
        directory_path = "/".join(directory_log)
        if directory_path in directories:
            directories[directory_path].append(file_size)
        else:
            directories[directory_path] = [file_size]

    directory_names = list(directories.keys())
    while len(directory_names) > 0:
        # Calculate the directories which are the furthest down in the directory tree first (do not contain any
        # other directories which we do not know the size of yet)
        # This is more efficient than calculating the directory sizes recursively each time
        directory_name = max(directory_names, key=directory_levels.get)
        size = calculate_directory_size(directory_name, directories, directory_sizes)
        directory_sizes[directory_name] = size
        directory_names.remove(directory_name)

    total_sizes = 0
    for directory in directories.keys():
        size = directory_sizes[directory]
        if size < 100000:
            total_sizes += size

    print(f"Part 1: Sum of total sizes = {total_sizes}")

    free_space = 70000000 - directory_sizes["/"]
    space_needed = 30000000 - free_space
    smallest_sufficient_size = 30000000

    for directory in directories.keys():
        # Check if size of the directory is large enough and a better solution
        if space_needed <= directory_sizes[directory] < smallest_sufficient_size:
            smallest_sufficient_size = directory_sizes[directory]

    print(f"Size of the smallest directory to delete = {smallest_sufficient_size}")


if __name__ == "__main__":
    main()
