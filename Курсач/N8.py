rubik = [int(x) for x in input("Enter rubik\n").split()]
print(rubik)

to_turn = []


def turn_try(matrix):
    equal = True
    i = 0
    while equal and i < 8:
        if matrix[i][0] != matrix[(i + 2) % 8][1] or\
                matrix[i + 1][0] != matrix[(i + 3) % 8][1]:
            equal = False
        i += 2
    if not equal:
        equal = True
        i = 0
        while equal and i > -8:
            if matrix[i % 8][0] != matrix[(i - 2) % 8][1] or\
                    matrix[(i + 1) % 8][0] != matrix[(i - 1) % 8][1]:
                equal = False
            i -= 2
    answer = ""
    if equal:
        answer = "Yes"
    else:
        answer = "NO"
    return answer


if rubik[12] == rubik[13] == rubik[14] == rubik[15] and\
        rubik[16] == rubik[17] == rubik[18] == rubik[19]:
    to_turn.append([rubik[0], rubik[1]])
    to_turn.append([rubik[2], rubik[3]])
    to_turn.append([rubik[4], rubik[5]])
    to_turn.append([rubik[6], rubik[7]])
    to_turn.append([rubik[8], rubik[9]])
    to_turn.append([rubik[10], rubik[11]])
    to_turn.append([rubik[21], rubik[20]])
    to_turn.append([rubik[23], rubik[22]])
    print(turn_try(to_turn))
elif rubik[0] == rubik[1] == rubik[2] == rubik[3] and\
        rubik[8] == rubik[9] == rubik[10] == rubik[11]:
    to_turn.append([rubik[14], rubik[12]])
    to_turn.append([rubik[15], rubik[13]])
    to_turn.append([rubik[6], rubik[4]])
    to_turn.append([rubik[7], rubik[5]])
    to_turn.append([rubik[18], rubik[16]])
    to_turn.append([rubik[19], rubik[17]])
    to_turn.append([rubik[22], rubik[20]])
    to_turn.append([rubik[23], rubik[21]])
    print(turn_try(to_turn))
elif rubik[4] == rubik[5] == rubik[6] == rubik[7] and\
         rubik[20] == rubik[21] == rubik[22] == rubik[23]:
    to_turn.append([rubik[2], rubik[0]])
    to_turn.append([rubik[3], rubik[1]])
    to_turn.append([rubik[16], rubik[17]])
    to_turn.append([rubik[18], rubik[19]])
    to_turn.append([rubik[9], rubik[11]])
    to_turn.append([rubik[8], rubik[10]])
    to_turn.append([rubik[15], rubik[14]])
    to_turn.append([rubik[13], rubik[12]])
    print(turn_try(to_turn))
else:
    print("NO")
