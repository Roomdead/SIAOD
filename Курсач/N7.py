import random
import math

def quickSort(arr):
    if len(arr) > 1:
        x = arr[random.randint(0, len(arr) - 1)]
        low = [item for item in arr if item < x]
        eq = [item for item in arr if item == x]
        hi = [item for item in arr if item > x]
        arr = quickSort(low) + eq + quickSort(hi)
    return arr


bn, ln = [int(x) for x in input("Enter number of brains and links\n").split()]
print("First number is {} and second number is {}".format(bn, ln))
links = []
for l in range(ln):
    links.append([int(x) for x in input('Enter {} pair of brains with link'
                                        ' between\n'.format(l + 1)).split()])
print(links)
vertexes = []
for el in links:
    for i in el:
        if not vertexes.count(i):
            vertexes.append(i)
vertexes = quickSort(vertexes)

matrix = list()
for _ in range(len(vertexes)):
    row = list()
    for _ in range(len(vertexes)):
        row.append(math.inf)
    matrix.append(row)
for edge in links:
    matrix[edge[0] - 1][edge[1] - 1] = 1
    matrix[edge[1] - 1][edge[0] - 1] = 1


def get_longest_path(matrix):
    path = 0
    for line in matrix:
        for el in line:
            if el > path:
                path = el
    return path


def floyd(matrix): #Сложность = n^3
    V = matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == math.inf and i == j:
                V[i][j] = 0
            else:
                V[i][j] == matrix[i][j]
    N = len(V)
    P = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if V[i][j] != math.inf:
                P[i][j] = j
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if V[i][j] != math.inf:
                for k in range(N):
                    if i == k or j == k: continue
                    if V[i][k] > V[i][j] + V[j][k]:
                        V[i][k] = V[i][j] + V[j][k]
                        P[i][k] = P[i][j]
    path = get_longest_path(matrix)
    return path


delay = floyd(matrix)
for line in matrix:
    print(line)
print("Delay =",delay)
