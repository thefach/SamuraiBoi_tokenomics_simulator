from liquiditypool import  LiquidityPool
from player import Player

import sys

# Open a text file to write the output
with open('output.txt', 'w') as f:
    # Redirect stdout to the file
    sys.stdout = f

    def print_lp_status(liqpool):

        print("\ncurrent XXX price:{} ".format(liqpool.get_xxx_price()))
        print("current MATIC ammount:{} ".format(liqpool.get_matic_ammount()))
        print("current XXX ammount:{} \n".format(liqpool.get_xxx_ammount()))


    # Create a liquidity pool with initial reserves
    lp = LiquidityPool(initial_matic=10000, initial_xxx=5000)

    print_lp_status(lp)

    # Create players with some initial MATIC
    player1 = Player(player_id=1, name="Nick", initial_matic=500)
    player2 = Player(player_id=2, name="Bob", initial_matic=300)
    player3 = Player(player_id=2, name="Miriam", initial_matic=1000)

    # Players buy XXX tokens
    player1.buy_xxx(liquidity_pool=lp, matic_amount=100)  
    print_lp_status(lp)
    player2.buy_xxx(liquidity_pool=lp, matic_amount=100)   
    print_lp_status(lp)
    player3.buy_xxx(liquidity_pool=lp, matic_amount=100)   

    # Players sell XXX tokens
    player1.sell_xxx(liquidity_pool=lp, xxx_amount=20)  
    print_lp_status(lp)
    player2.sell_xxx(liquidity_pool=lp, xxx_amount=10)  
    print_lp_status(lp)
    player3.sell_xxx(liquidity_pool=lp, xxx_amount=10)  
    print_lp_status(lp)

    # Players buy XXX tokens
    player1.buy_xxx(liquidity_pool=lp, matic_amount=100)  
    print_lp_status(lp)
    player2.buy_xxx(liquidity_pool=lp, matic_amount=100)   
    print_lp_status(lp)


    # Players mint NFTs
    player1.mint_nft(liquidity_pool=lp, matic_amount=100)  
    print_lp_status(lp)
    player2.mint_nft(liquidity_pool=lp, matic_amount=50) 
    print_lp_status(lp)

    print(player1)
    print(player2)
    print(player3)
    
    # Your script or code that prints to console
    print("This will be written in the output.txt file")
    print("Another line in the text file")
    
# Reset stdout back to its original state (if needed for further printing to console)
sys.stdout = sys.__stdout__



