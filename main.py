import item
import player as Player

# Beginning story
print('You find yourself in a vast and dark forest')
print('There should be a temple around here with some treasures')
print()

# Create player
# Add item.oneHit() as an argument if you want a cheat to test the game
player = Player.player(100, 0, 0, 0, item.stick(), item.apple())

# Initialize first room
player.map.getTile(0, 0, 0).enter(player)

# Main gameplay loop
while player.playing:
    player.printActions()
    player.action(input())
    print()
