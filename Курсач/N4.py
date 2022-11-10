def recieve():
    print("Введите число матриц")
    t = int(input())
    matr = []
    synt = {'.', '#', 'K'}
    for i in range(t):
        matr.append([])
        numb = 0
        j = 0
        while j < 8:
            print("Введите", j + 1, "строку матрицы", i + 1)
            string = input()
            if len(string) == 8:
                symb = set(string)
                if symb <= synt:
                    if string.count('K') >= 0:
                        numb += string.count('K')
                        if numb > 2:
                            numb -= 1
                            print('Превышено допустимое число полуконей')
                        else:
                            matr[i].append(string)
                            j += 1
                    else:
                        matr[i].append(string)
                        j += 1
                else:
                    print("Строка введена неверно")
            else:
                print("Строка введена неверно")
            if j == 8 and numb < 2:
                print("Недостаточно полуконей:", numb)
                matr[i].pop()
                j -= 1
    return matr


def search(matrix):
    i = 0
    hh1 = []
    hh2 = []
    horses = []
    found = False
    while i < 8 and not found:
        j = 0
        while j < 8 and not found:
            if matrix[i][j] == 'K':
                if not hh1:
                    hh1.append(i)
                    hh1.append(j)
                else:
                    hh2.append(i)
                    hh2.append(j)
                    found = True
            j += 1
        i += 1
    horses.append(hh1)
    horses.append(hh2)
    return horses


def analize(horses):
    hh1 = horses[0]
    hh2 = horses[1]
    for i in range(2):
        for j in range(2):
            hh1[0] += 2 * (-1) ** i
            hh1[1] += 2 * (-1) ** j
            if hh1[0] < 8 and hh1[1] < 8:
                if hh1 == hh2:
                    return 'Yes'
                else:
                    for m in range(2):
                        for n in range(2):
                            hh2[0] += 2 * (-1) ** m
                            hh2[1] += 2 * (-1) ** n
                            if hh1[0] < 8 and hh1[1] < 8:
                                if hh1 == hh2:
                                    return 'Yes'
    return 'No'


matrix = recieve()
for i in range(len(matrix)):
    print("Matrix:", i + 1, "answer:", analize(search(matrix[i])))
