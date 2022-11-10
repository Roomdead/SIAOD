n = int(input())
s = "01100000"
t = "10010011"


def sol(n, s, t):
    pairs = {'11': 0, '10': 0, '01': 0, '00': 0}
    first = 0
    second = 0
    for i in range(2 * n):
        pairs[str(s[i]) + str(t[i])] += 1
    print(pairs)
    first += pairs['10'] + pairs['11'] // 2
    second += pairs['01'] + pairs['11'] // 2
    if pairs['11'] % 2:
        first += 1
    print(first, second)
    if first == second:
        ans = 'Draw'
    elif first > second:
        ans = 'First'
    else:
        ans = 'Second'
    return ans


print(sol(n, s, t))
