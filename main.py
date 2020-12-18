import item
import player as Player

#Beginning story
print('You find yourself in a vast and dark forest')
print('There should be a temple around here with some treasures')
print()

player = Player.player(100, 0, 0, 0, item.stick(), item.apple())
# add item.oneHit() as an argument above if u want to skip combat 

while player.playing:
    player.printActions()
    player.action(input())
    print()
