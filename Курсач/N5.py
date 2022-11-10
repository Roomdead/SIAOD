n = 0
k = 0
while not (n >= 1 and n <= 1000):
    print('Введите число n')
    n = int(input())
minimal = min(8, n)
while not (k >= 1 and k <= minimal):
    print('Введите число k')
    k = int(input())
print(((k ** (k-1)) * ((n-k) ** (n-k))) % 1000000007)
