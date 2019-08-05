from DAY_10.game import Character, Barbarian


#PRZYPISUJEMY DLA PLAYER'A WARTOSC 20 DLA HEALTH, ENEMY ZOSTAJE BEZ ZMIAN
player = Character(20)
enemy = Character()

barbarian = Barbarian()

print(f"Before attack player has armor {player.armor} and health {player.health}")

#enemy przejmuje wartosci player'a - zostana nadpisane
#enemy.attack(player)

#atakujemy 20 razy player'a

# for i in range(50):
#     if player.character_state == 'Dead':
#         break
#     enemy.attack(player)

barbarian.attack(player)

print(f"After attack player has armor {player.armor} and health {player.health}")



print(player.health)





# my_brand_new_dice = Dice()
# my_brand_new_dice.roll()