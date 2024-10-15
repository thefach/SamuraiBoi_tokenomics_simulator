from liquiditypool import  LiquidityPool
from player import Player


def print_lp_status(liqpool):

    print("\ncurrent XXX price:{} ".format(liqpool.get_xxx_price()))
    print("current MATIC ammount:{} ".format(liqpool.get_matic_ammount()))
    print("current XXX ammount:{} \n".format(liqpool.get_xxx_ammount()))


# Create a liquidity pool with initial reserves
lp = LiquidityPool(initial_matic=10000, initial_xxx=5000)

print_lp_status(lp)

# Create players with some initial MATIC
player1 = Player(player_id=1, name="Alice", initial_matic=500)
player2 = Player(player_id=2, name="Bob", initial_matic=300)

# Players buy XXX tokens
player1.buy_xxx(liquidity_pool=lp, matic_amount=100)  # Alice buys XXX tokens
print_lp_status(lp)
player2.buy_xxx(liquidity_pool=lp, matic_amount=100)   # Bob buys XXX tokens
print_lp_status(lp)


# Players sell XXX tokens
player1.sell_xxx(liquidity_pool=lp, xxx_amount=20)  # Alice sells some XXX tokens
print_lp_status(lp)
player2.sell_xxx(liquidity_pool=lp, xxx_amount=10)  # Bob sells some XXX tokens
print_lp_status(lp)

# Players buy XXX tokens
player1.buy_xxx(liquidity_pool=lp, matic_amount=100)  # Alice buys XXX tokens
print_lp_status(lp)
player2.buy_xxx(liquidity_pool=lp, matic_amount=100)   # Bob buys XXX tokens
print_lp_status(lp)


# Players mint NFTs
player1.mint_nft(liquidity_pool=lp, matic_amount=100)  # Alice mints an NFT
print_lp_status(lp)
player2.mint_nft(liquidity_pool=lp, matic_amount=50) 
print_lp_status(lp)




print(player1)



