import random


users = ["krzysiek", "mietek", "rafal","weronika", "agata", "franek", "olek"]


groups = []

if len(users) % 2 == 0:
    while len(users) > 0:
        duet = random.sample(users, 2)
        groups.append(duet)
        users.remove(duet[0])
        users.remove(duet[1])
else:
    while len(users) > 1:
        duet = random.sample(users, 2)
        groups.append(duet)
        users.remove(duet[0])
        users.remove(duet[1])
    groups[-1].append(users[0]) # add last member

print(groups)
