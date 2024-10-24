from maps_objects import  Map
from player import Player

import sys

# Open a text file to write the output
with open('test_game_output.txt', 'w') as f:
    # Redirect stdout to the file
    sys.stdout = f

    # Create players and a map
    alice = Player(player_id=1, name="Alice", initial_matic=1000)
    bob = Player(player_id=2, name="Bob", initial_matic=1200)
    map1 = Map(map_id=1, difficulty="Medium")

    # Give players some XXX tokens
    alice.update_wallet('XXX', 5)
    bob.update_wallet('XXX', 5)

    # Players play on the map
    alice.play(map1)
    print(" ")
    bob.play(map1)
    print(" ")
    alice.play(map1)  # Alice plays again
    print(" ")
    alice.play(map1)
    print(" ")
    bob.play(map1)
    print(" ")
    alice.play(map1)  # Alice plays again
    print(" ")
      
    # Print map and player details
    print(map1)
    print(alice)
    print(bob)

# Reset stdout back to its original state (if needed for further printing to console)
sys.stdout = sys.__stdout__
