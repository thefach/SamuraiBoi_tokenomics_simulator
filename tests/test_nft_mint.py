from systemfeedeposit import  SystemFeeDeposit
from player import Player
from map import  Map
from devwallet import DevWallet

# Create players, a map, a system fee deposit, and a dev wallet
alice = Player(player_id=1, name="Alice", initial_matic=1000)
bob = Player(player_id=2, name="Bob", initial_matic=1200)
map1 = Map(map_id=1, difficulty="Medium")
system_fee_deposit = SystemFeeDeposit()
dev_wallet = DevWallet()

# Give players some XXX tokens
alice.update_wallet('XXX', 5)
bob.update_wallet('XXX', 5)

# Players play on the map
alice.play(map1, system_fee_deposit)
bob.play(map1, system_fee_deposit)

# Players mint NFTs
alice.mint_nft(dev_wallet)
bob.mint_nft(dev_wallet)

# Print map, player, system fee deposit, and dev wallet details
print(map1)
print(alice)
print(bob)
print(system_fee_deposit)
print(dev_wallet)
