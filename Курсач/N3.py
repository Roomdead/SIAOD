def sol(n, p1, p2):
    to_sort = []
    for i in range(n):
        to_sort.append(p2.index(p1[i]))
    print(to_sort)
    act_num = 0
    while not to_sort == sorted(to_sort):
        to_sort.pop()
        act_num += 1
    return act_num

n = 5
p1 = '15234'
p2 = '12345'
print(sol(n, p1, p2))
