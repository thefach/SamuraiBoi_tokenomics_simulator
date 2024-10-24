from player_objects import Player
from maps_objects import  MapRegistry
from systemfeedeposit import  SystemFeeDeposit
from player_objects import PlayerRegistry
from datetime import datetime, timedelta


# Example usage
player_registry = PlayerRegistry()
map_registry = MapRegistry()
system_fee_deposit = SystemFeeDeposit()

# Register new players
player_registry.register_player(player_id=1, name="Alice", initial_matic=1000)
player_registry.register_player(player_id=2, name="Bob", initial_matic=500)

# give them XXX
player_registry.get_player(1).update_wallet('XXX', 5)
player_registry.get_player(2).update_wallet('XXX', 5)

alice = player_registry.get_player(1)
bob = player_registry.get_player(2)

# Give Alice some NFTs
alice.nfts = 5

# Alice creates 2 maps
map_registry.register_map(map_id=101, difficulty="Medium", expiration_days=14, creator_id=1, locked_nfts=3)
map_registry.register_map(map_id=45, difficulty="Medium", expiration_days=14, creator_id=1, locked_nfts=3)
map1 = map_registry.get_map(101)
map2 = map_registry.get_map(45)



print(map1)
print(map2)
print(map_registry)
print("###############################################")
alice.play(map1, system_fee_deposit)
print(" ")
bob.play(map1, system_fee_deposit)
print(" ")
bob.play(map1, system_fee_deposit)
print(" ")
bob.play(map1, system_fee_deposit)
print(" ")
bob.play(map1, system_fee_deposit)
print(" ")
alice.play(map1, system_fee_deposit)  
print(" ")
print("###############################################")
print(map1)
print(map2)
print(map_registry)
print("###############################################")
print(map1.creator_id)
print(map1.best_player_id)

# Fast-forward in time to make the map expired (for testing purposes, adjust expiration_days to 0)
map1.creation_date -= timedelta(days=map1.expiration_days + 1)

print(" ")
print("###############################################")
# Simulate map expiration check
map_registry.check_expired_maps(player_registry)

# Print players' final state
print(alice)
print(bob)
