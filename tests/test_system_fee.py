from systemfeedeposit import  SystemFeeDeposit
from player import Player
from map import  Map

# Create players, a map, and a system fee deposit
alice = Player(player_id=1, name="Alice", initial_matic=1000)
bob = Player(player_id=2, name="Bob", initial_matic=1200)
map1 = Map(map_id=1, difficulty="Medium")
system_fee_deposit = SystemFeeDeposit()

# Give players some XXX tokens
alice.update_wallet('XXX', 5)
bob.update_wallet('XXX', 5)

# Players play on the map
alice.play(map1, system_fee_deposit)
bob.play(map1, system_fee_deposit)
alice.play(map1, system_fee_deposit)  # Alice plays again

# Print map, player, and system fee deposit details
print(map1)
print(alice)
print(bob)
print(system_fee_deposit)

