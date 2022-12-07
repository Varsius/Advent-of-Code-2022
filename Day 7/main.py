def calculate_directory_size(directory, directories, directory_sizes):

    size = 0

    for content in directories[directory]:
        if content.isnumeric():
            size += int(content)
        else:
            size += directory_sizes[content]

    return size

def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()

    directory_log = ["/"]
    directories = {}
    directory_levels = {"/": 1}
    directory_sizes = {}

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
            directory_levels[destination] = len(directory_log)
            continue

        if line.startswith("dir"):
            directory_name = line.split()[1]
            if directory_log[-1] in directories:
                directories[directory_log[-1]].append(directory_name)
            else:
                directories[directory_log[-1]] = [directory_name]
            continue

        if line.startswith("$ ls"):
            continue

        file_size = line.split()[0]
        if directory_log[-1] in directories:
            directories[directory_log[-1]].append(file_size)
        else:
            directories[directory_log[-1]] = [file_size]

    directory_names = list(directories.keys())
    while len(directory_names) > 0:

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

if __name__ == "__main__":
    main()