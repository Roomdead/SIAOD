import random


def quickSort(arr):
    if len(arr) > 1:
        x = arr[random.randint(0, len(arr) - 1)]
        low = [item for item in arr if item[1] < x[1]]
        eq = [item for item in arr if item[1] == x[1]]
        hi = [item for item in arr if item[1] > x[1]]
        arr = quickSort(hi) + eq + quickSort(low)
    return arr


name = input("Enter your name\n")
num = int(input("Enter number of actions\n"))
actions = []
for i in range(num):
    actions.append(input("Enter action\n").split())

# actions = [['ahmed', 'posted', 'on', 'fatma’s', 'wall'], ['fatma', 'commented', 'on', 'ahmed’s', 'post'], ['mona', 'likes', 'ahmed’s', 'post']]
# print(actions)
actors = []
rating = []
for act in actions:
    if not actors.count(act[0]):
        actors.append(act[0])

for actor in actors:
    if not actor == name:
        rating.append([actor, 0])

#print(actors)
for act in actions:
    fl = False
    for pers in range(len(rating)):
        if rating[pers][0] == act[0]:
            i = pers
            fl = True
        elif act[0] == name:
            for passive in range(len(rating)):
                # print(rating[passive][0] + "’s", ' ', act[len(act) - 2])
                if rating[passive][0] + "’s" == act[len(act) - 2]:
                    i = passive
                    fl = True
    if fl:
        if act[1] == 'posted':
            rating[i][1] += 15
        elif act[1] == 'commented':
            rating[i][1] += 10
        elif act[1] == 'likes':
            rating[i][1] += 5


sorted_rating = quickSort(rating)

for pers in sorted_rating:
    print(pers[0])
