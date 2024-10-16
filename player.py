import random

class Player:
    def __init__(self, player_id, name, initial_matic):
        self.player_id = player_id
        self.name = name
        self.matic_wallet = initial_matic  # Player's balance in MATIC
        self.xxx_wallet = 0  # Player's balance in XXX tokens
        self.nfts = 0  # Player's NFTs
        self.times_on_maps = {}  # Dictionary {map_id: [list of time_taken]}

    def __str__(self):
        """Define how to print a player's status."""
        map_times = ', '.join([f"Map {mid}: {times}" for mid, times in self.times_on_maps.items()]) or 'No times recorded'
        return (f"Player {self.name}:\n"
                f"  MATIC Wallet: {self.matic_wallet}\n"
                f"  XXX Wallet: {self.xxx_wallet}\n"
                f"  NFTs Owned: {self.nfts}\n"
                f"  Times on Maps: {map_times}")

    # Game actions

    def play(self, game_map):
        """Play on the map by paying 1 XXX token and setting a random time."""
        if self.xxx_wallet >= 1:
            self.update_wallet('XXX', -1)  # Deduct 1 XXX token from player's wallet
            time_taken = random.randint(0, 300)  # Random time between 0 and 300 seconds
            
            # Store the time for this map, create a list if it's the player's first time on the map
            if game_map.map_id not in self.times_on_maps:
                self.times_on_maps[game_map.map_id] = []
            self.times_on_maps[game_map.map_id].append(time_taken)  # Add the new time

            game_map.update_player_time(self, time_taken)  # Update the map with the player's time
            game_map.add_xxx_to_pool(1)  # Add the 1 XXX to the map's pool
            print(f"{self.name} played on Map {game_map.map_id} and took {time_taken} seconds.")
        else:
            print(f"{self.name} does not have enough XXX tokens to play on Map {game_map.map_id}.")

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


