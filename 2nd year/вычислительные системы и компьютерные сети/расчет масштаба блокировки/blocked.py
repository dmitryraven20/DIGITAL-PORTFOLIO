s, part = 0, []
input_list = open("input.txt", "r")
lines = input_list.readlines()
for line in lines:
    part1, part2 = line.split('/')
    if len(part2) > 1:
        part.append(int(part2[:2]))
input_list.close
for i in part:
    s += 2 ** (32 - i)
print(s)