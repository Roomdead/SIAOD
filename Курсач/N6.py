name = input("Enter your name\n")
num = int(input("Enter number of actions\n"))
actions = []
for i in range(num):
    actions.append(input("Enter action\n").split())
print(actions)
actors = []
rating = []
for act in actions:
    if not actors.count(act[0]):
        actors.append(act[0])

for actor in actors:
    rating.append([actor, 0])

print(actors)
for act in actions:
    i = -1
    for pers in range(len(rating)):
        if rating[pers][0] == act[0]:
            i = pers
            if act[0] == name:
                for passive in range(len(rating)):
                    if rating[passive][0] + "'s" == act[len(act) - 2]:
                        i = passive
    if i:
        if act[1] == 'posted':
            rating[i][1] += 15
        elif act[1] == 'commented':
            rating[i][1] += 10
        elif act[1] == 'likes':
            rating[i][1] += 5

print(rating)


