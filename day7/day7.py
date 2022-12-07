from collections import defaultdict
from functools import cache

OutputList = []
with open("day7/input.txt", "r") as data:
    for t in data:
        Line = t.strip()
        LineList = Line.split()
        LineTuple = tuple(LineList)
        OutputList.append(LineTuple)

DirectoryDict = defaultdict()
DirectorySet = set()
DirectoryStack = []
CurrentDirList = []
ListMode = False

for o in OutputList:
    if o[1] == "cd":
        if ListMode:
            DirectoryContentsTuple = tuple(CurrentDirList)
            DirectoryDict[CurrentDirectory] = DirectoryContentsTuple
            CurrentDirList.clear()
            ListMode = False
        if o[2] == "..":
            DirectoryStack.pop()
            CurrentDirectory = tuple(DirectoryStack)
        else:
            DirectoryStack.append(o[2])
            CurrentDirectory = tuple(DirectoryStack)
            DirectorySet.add(CurrentDirectory)
    elif o[1] == "ls":
        ListMode = True
    elif o[0] == "dir":
        DirectoryStack.append(o[1])
        NewDirectoryTuple = tuple(DirectoryStack)
        CurrentDirList.append(NewDirectoryTuple)
        DirectoryStack.pop()
    else:
        NewFileTuple = (int(o[0]), "File", o[1])
        CurrentDirList.append(NewFileTuple)

if ListMode:
    DirectoryContentsTuple = tuple(CurrentDirList)
    DirectoryDict[CurrentDirectory] = DirectoryContentsTuple
    CurrentDirList.clear()
    ListMode = False

@cache
def CalculateDirectorySize(Directory):
    CurrentSize = 0
    NewList = DirectoryDict[Directory]
    for y in NewList:
        if y[1] == "File":
            CurrentSize += y[0]
        else:
            CurrentSize += CalculateDirectorySize(y)
    return CurrentSize

Part1Answer = 0
for d in DirectorySet:
    NewValue = CalculateDirectorySize(d)
    if len(d) == 1:
        OuterShell = NewValue
    if NewValue <= 100000:
        Part1Answer += NewValue

UnusedSpace = 70000000 - OuterShell
CurrentDeletionSize = 1000000000000000000000
for d in DirectorySet:
    NewValue = CalculateDirectorySize(d)
    if (UnusedSpace + NewValue) >= 30000000 and NewValue < CurrentDeletionSize:
        CurrentDeletionSize = NewValue

Part2Answer = CurrentDeletionSize

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")