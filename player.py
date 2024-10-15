class Player:
    def __init__(self, player_id, name, initial_matic):
        self.player_id = player_id
        self.name = name
        self.matic_wallet = initial_matic  # Player's balance in MATIC
        self.xxx_wallet = 0  # Player's balance in XXX tokens
        self.nfts = 0  # Player's NFTs
        self.time = None  # Time for the current map challenge

    def __str__(self):
        """Define how to print a player's status."""
        return (f"Player {self.name}:\n"
                f"  MATIC Wallet: {self.matic_wallet}\n"
                f"  XXX Wallet: {self.xxx_wallet}\n"
                f"  NFTs Owned: {self.nfts}\n"
                f"  Challenge Time: {self.time if self.time else 'Not set'}")

    # Game actions
    
    def set_time(self, time_taken):
        """Set the time taken by the player for the challenge."""
        self.time = time_taken

    # Economic actions

    def update_wallet(self, token_type, amount):
        """Update the player's wallet for MATIC or XXX tokens."""
        if token_type == 'MATIC':
            self.matic_wallet += amount
        elif token_type == 'XXX':
            self.xxx_wallet += amount

    def buy_xxx(self, liquidity_pool, matic_amount):
        """Buy XXX tokens by spending MATIC through the liquidity pool."""
        if self.matic_wallet >= matic_amount:
            xxx_bought = liquidity_pool.swap_matic_for_xxx(matic_amount)
            self.update_wallet('MATIC', -matic_amount)  # Deduct MATIC spent
            self.update_wallet('XXX', xxx_bought)  # Add XXX tokens bought
            print(f"{self.name} bought {xxx_bought} XXX tokens for {matic_amount} MATIC.")
        else:
            print(f"{self.name} does not have enough MATIC to buy XXX tokens.")

    def sell_xxx(self, liquidity_pool, xxx_amount):
        """Sell XXX tokens for MATIC through the liquidity pool."""
        if self.xxx_wallet >= xxx_amount:
            matic_bought = liquidity_pool.swap_xxx_for_matic(xxx_amount)
            self.update_wallet('XXX', -xxx_amount)  # Deduct XXX sold
            self.update_wallet('MATIC', matic_bought)  # Add MATIC earned
            print(f"{self.name} sold {xxx_amount} XXX tokens for {matic_bought} MATIC.")
        else:
            print(f"{self.name} does not have enough XXX tokens to sell.")

    def mint_nft(self, liquidity_pool, matic_amount):
        """Mint an NFT by spending MATIC through the liquidity pool."""
        if self.matic_wallet >= matic_amount:
            success = liquidity_pool.mint_nft(matic_amount)
            if success:
                self.update_wallet('MATIC', -matic_amount)  # Deduct MATIC for minting NFT
                self.nfts += 1  # Add 1 NFT to player's wallet
                print(f"{self.name} minted an NFT for {matic_amount} MATIC.")
            else:
                print(f"{self.name} does not have enough MATIC to mint an NFT.")
        else:
            print(f"{self.name} does not have enough MATIC to mint an NFT.")
