from player import Player
from player import PlayerRegistry

# Example usage
player_registry = PlayerRegistry()

# Register new players
player_registry.register_player(player_id=1, name="Alice", initial_matic=1000)
player_registry.register_player(player_id=2, name="Bob", initial_matic=500)

# Retrieve and print a player instance by their ID
player = player_registry.get_player(1)
if player:
    print(player)
else:
    print("Player not found.")

print("################################")
print(player)
player_registry.get_player(1).update_wallet('XXX', 5)
print(player)
# Print all players in the registry
#print(player_registry)