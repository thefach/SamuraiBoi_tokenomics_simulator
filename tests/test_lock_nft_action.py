from player_objects import Player
from maps_objects import  MapRegistry

# Create players and a map registry
alice = Player(player_id=1, name="Alice", initial_matic=1000)
alice.nfts = 5  # Alice has 5 NFTs

map_registry = MapRegistry()

# Alice creates a map
map1 = alice.create_map(map_registry)

# Print the map and map registry details
if map1:
    print(map1)
print(map_registry)


method_list = [func for func in dir(MapRegistry) if callable(getattr(MapRegistry, func)) and not func.startswith("__")]
print(method_list)