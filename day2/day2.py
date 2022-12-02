#Load the puzzle data
with open('day2/input.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

#Part 1
wins = ['A Y', 'B Z', 'C X']
draws = ['A X', 'B Y', 'C Z']
score = 0
for line in data:
    if line in wins:
        score += 6
    elif line in draws:
        score += 3
    score += ' XYZ'.index(line.split()[1])
print("Part 1: ")
print(score)

#Part 2
score = 0
for line in data:
    elf, me = line.split()
    if me == 'Y':
        score += 3 + ' ABC'.index(elf)
    elif me == 'Z':
        score += 6 + ' CAB'.index(elf)
    else:
        score += ' BCA'.index(elf)
print("Part 2: ")
print(score)