import item
import player as Player
import map

player = Player.player(100, 0, 0, 0, item.woodenStick(), item.apple())
while player.alive:
    player.printActions()
    player.action(input())
    print()
