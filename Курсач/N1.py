c, d = int(input()), int(input())
n, m = int(input()), int(input())
k = int(input())
def sol(c, d ,n, m ,k):
    ans = 0
    if not k >= n * m:
        main_price = c / n
        add_price = float(d)
        if add_price <= main_price:
            ans = d(n * m - k)
        else:
            exact = d * ((n * m - k) % n) + c * ((n * m - k) // n)
            approx = c * ((n * m - k) // n + 1)
            ans = min(exact, approx)
    return ans


print(sol(c, d, n, m, k))
