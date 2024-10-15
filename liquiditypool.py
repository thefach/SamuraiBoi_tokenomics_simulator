"""
LiquidityPool Class
This class will simulate a liquidity pool where players can exchange MATIC
for XXX tokens and handle token reserves. The pool will also support minting NFTs for MATIC.
"""

class LiquidityPool:
    def __init__(self, initial_matic, initial_xxx):
        self.matic_reserve = initial_matic
        self.xxx_reserve = initial_xxx
        self.nfts = 0  # Number of NFTs minted

    def get_matic_ammount(self):
        """Calculate the price of XXX tokens in terms of MATIC (e.g., constant product formula)."""
        return self.matic_reserve 
    
    def get_xxx_ammount(self):
        """Calculate the price of XXX tokens in terms of MATIC (e.g., constant product formula)."""
        return  self.xxx_reserve
    
    def get_xxx_price(self):
        """Calculate the price of XXX tokens in terms of MATIC (e.g., constant product formula)."""
        return self.matic_reserve / self.xxx_reserve

    def swap_matic_for_xxx(self, matic_amount):
        """Perform the token swap from MATIC to XXX."""
        xxx_bought = matic_amount / self.get_xxx_price()
        self.matic_reserve += matic_amount
        self.xxx_reserve -= xxx_bought
        return xxx_bought
    
    def swap_xxx_for_matic(self, xxx_amount):
        """Perform the token swap from XXX to MATIC.""" 
        matic_bought = xxx_amount / self.get_xxx_price()
        self.xxx_reserve += xxx_amount
        self.matic_reserve -= matic_bought
        return matic_bought

    def mint_nft(self, matic_amount):
        """Mint an NFT by burning MATIC."""
        nft_price = 100  # Define an arbitrary price for NFT in MATIC
        if matic_amount >= nft_price:
            self.matic_reserve += matic_amount
            self.nfts += 1
            return True  # NFT minted
        return False  # Not enough MATIC to mint NFT



