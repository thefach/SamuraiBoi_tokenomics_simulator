class DevWallet:
    def __init__(self):
        self.total_matic = 0  # Total MATIC accumulated from NFT minting
        self.nft_price = 10  # Price of minting an NFT in MATIC

    def add_matic(self, amount):
        """Add MATIC to the developer wallet."""
        self.total_matic += amount

    def get_nft_price(self):
        """Get the price of minting an NFT."""
        return self.nft_price

    def __str__(self):
        """Define how to print the total MATIC in the dev wallet."""
        return f"Total MATIC in Dev Wallet: {self.total_matic}"
