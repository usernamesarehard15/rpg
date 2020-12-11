import item
import player as Player
import map

player = Player.player(100,0,0,0,item.apple(),item.bandages())
while player.alive:
    player.action(input())
    print()
player.printMap(map.map, 0)


