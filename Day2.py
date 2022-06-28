#Part 1


with open("Day2_files", "r") as f: #just change the file path to yours where it says Day2_files. Store your puzzle input in txt.
    depth = 0
    horizontal = 0
    lines = f.readlines()
    for line in lines:
        if "forward" in line:
            horizontal = horizontal + int((line.strip(" ")[8]))
        if "down" in line:
            depth = depth + int((line.strip(" ")[5]))
        if "up" in line:
            depth = depth - int((line.strip(" ")[3]))


print("Horizontal Value:", horizontal)
print("Depth Value:", depth)

Answer_of_day2 = horizontal * depth
print(Answer_of_day2)





#Part 2


with open("Day2_files", "r") as f: #  change the file path here too to your file path where it says Day2_files.
    depth = 0
    horizontal = 0
    aim = 0
    lines = f.readlines()
    for line in lines:
        if "forward" in line:
            forward_val = int((line.strip(" ")[8]))
            horizontal += forward_val
            depth += aim * forward_val

        if "down" in line:
            aim += int((line.strip(" ")[5]))

        if "up" in line:
            aim -= int((line.strip(" ")[3]))

print(horizontal * depth)
