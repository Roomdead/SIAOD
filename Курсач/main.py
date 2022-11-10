def solution(N, L, R, C):
    lcnt = []
    rcnt = []
    for i in range(N+1):
        lcnt.append(0)
        rcnt.append(0)
    for i in range(N):
        if i < L:
            lcnt[C[i]] += 1
        else:
            rcnt[C[i]] += 1
    for i in range(N):
        mn = min(lcnt[i], rcnt[i])
        print(mn)
        lcnt[i] -= mn
        rcnt[i] -= mn
        L -= mn
        R -= mn
    print(L, R)
    if L < R:
        lcnt, rcnt = rcnt, lcnt
        L, R = R, L
    ans = 0
    for i in range(N):
        extra = L - R
        can_do = lcnt[i]//2
        print(can_do)
        do = min(can_do*2, extra)
        ans += do//2
        L -= do
    ans += (L - R)/2 + (L + R)/2
    return ans


N, L, R = int(input()), int(input()), int(input())
#C = [6, 5, 4, 3, 2, 1]
#C = [1, 1, 2, 2, 2, 2]
#C = [1, 2, 3, 2, 2, 2]
C = [4, 4, 4, 3]
print(solution(N, L, R, C))
