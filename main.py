import item
import player as Player

player = Player.player(100, 0, 0, 0, item.stick(), item.apple(), item.oneHit())
# add item.oneHit() as an argument above if u want to skip combat 


while player.playing:
    player.printActions()
    player.action(input())
    print()
