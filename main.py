import item
import player as Player

player = Player.player(100, 0, 0, 0, item.stick(), item.apple(), item.oneHit())

while player.playing:
    player.printActions()
    player.action(input())
    print()
