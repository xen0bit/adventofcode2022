from pprint import pprint
input = []
with open('day1/input.txt', 'r') as f:
    temp = []
    for line in f:
        stripped = line.replace("\n", "")
        if stripped != "":
            temp.append(int(stripped))
        else:
            input.append(temp)
            temp = []
    input.append(temp)

sums = []

for item in input:
    sums.append(sum(item))

sums.sort()

print(sums)

print(sum(sums[len(sums)-3:]))