import item
import player

player = player.player(100,item.apple(),item.bandages())
while True:
	player.action(input())
	print()
