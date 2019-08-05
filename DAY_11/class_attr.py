class Fight(object):
    random_chance = 0.7

    def __init__(self):
        pass


fights = [Fight(), Fight(), Fight()]

for fight in fights:
    print(fight.random_chance)


Fight.random_chance = 0.8
fights[0].random_chance = 0.3


for fight in fights:
    print(fight.random_chance)
