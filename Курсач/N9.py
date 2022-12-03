import random


length = int(input("Type a number of segments\n"))
segments = []
for i in range(length):
    segments.append([int(x) for x in input("Enter segment {}\n".format(i + 1)).split()])
for el in segments:
    el.sort()


def quickSort(arr):
    if len(arr) > 1:
        x = arr[random.randint(0, len(arr) - 1)]
        low = [item for item in arr if item[0] < x[0]]
        eq = [item for item in arr if item[0] == x[0]]
        hi = [item for item in arr if item[0] > x[0]]
        arr = quickSort(low) + SideQuickSort(eq) + quickSort(hi)
    return arr


def SideQuickSort(arr):
    if len(arr) > 1:
        x = arr[random.randint(0, len(arr) - 1)]
        low = [item for item in arr if item[1] < x[1]]
        eq = [item for item in arr if item[1] == x[1]]
        hi = [item for item in arr if item[1] > x[1]]
        arr = quickSort(hi) + eq + quickSort(low)
    return arr


SortedSegments = quickSort(segments)


def SerchPos(arr):
    pos = [-1, -1]
    MaxRightBorder = arr[0][1]
    MaxRightBorderPos = 0
    found = False
    i = 0
    while i < len(arr) - 1 and not found:
        i += 1
        if arr[i][1] > MaxRightBorder:
            MaxRightBorder = arr[i][1]
            MaxRightBorderPos = i
        else:
            pos = [segments.index(arr[i]) + 1, segments.index(arr[MaxRightBorderPos]) + 1]
            found = True
    return pos

out = SerchPos(SortedSegments)
print(out[0], out[1])
