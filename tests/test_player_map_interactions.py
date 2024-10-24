from player import Player
from maps_objects import  MapRegistry

# Create players and a map registry
alice = Player(player_id=1, name="Alice", initial_matic=1000)
print(alice)
map_registry = MapRegistry()
print(map_registry)

# Alice creates two maps
map1 = alice.create_map(map_registry) # create map sets all the necessary map parameters (randomly when needed)
print(map1)
map2 = alice.create_map(map_registry)
print(map1)


# Print the map registry details
print(map_registry)
print(alice)
