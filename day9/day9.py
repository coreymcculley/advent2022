import numpy as np


def move(knots, move):
    knots[0] += move

    for prev_knot, curr_knot in zip(knots, knots[1:]):
        if max(abs(prev_knot - curr_knot)) > 1:
            curr_knot += np.clip((prev_knot - curr_knot), -1, 1)


def solve(x, k):
    knots = [np.array([0, 0]) for _ in range(k)]
    positions = set()
    shift = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L':(0, -1)}

    for line in x:
        direc, steps = line.split(" ")
        for _ in range(int(steps)):
            move(knots, shift[direc])
            positions.add(tuple(knots[-1]))

    return len(positions)


x = open("day9/input.txt").readlines()

print("Part1: ",solve(x, 2))
print("Part2: ",solve(x, 10))