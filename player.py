import random
from datetime import datetime
from maps_objects import  Map

class Player:
    def __init__(self, player_id, name, initial_matic):
        self.player_id = player_id
        self.name = name
        self.matic_wallet = initial_matic  # Player's balance in MATIC
        self.xxx_wallet = 0  # Player's balance in XXX tokens
        self.nfts = 0  # Player's NFTs
        self.times_on_maps = {}  # Dictionary {map_id: [list of time_taken]}
        self.matic_fees_paid = 0  # Total fees paid by the player in MATIC

    def __str__(self):
        """Define how to print a player's status."""
        map_times = ', '.join([f"Map {mid}: {times}" for mid, times in self.times_on_maps.items()]) or 'No times recorded'
        return (f"Player {self.name}:\n"
                f"  MATIC Wallet: {self.matic_wallet}\n"
                f"  XXX Wallet: {self.xxx_wallet}\n"
                f"  NFTs Owned: {self.nfts}\n"
                f"  Times on Maps: {map_times}\n"
                f"  MATIC Fees Paid: {self.matic_fees_paid}")

    # Game actions

    def play(self, game_map, system_fee_deposit):
        """Play on the map by paying 1 XXX token and a system fee in MATIC, setting a random time."""
        system_fee = system_fee_deposit.get_fee()

        if self.xxx_wallet >= 1 and self.matic_wallet >= system_fee:
            # Deduct the required tokens and fees
            self.update_wallet('XXX', -1)  # Deduct 1 XXX token from player's wallet
            self.update_wallet('MATIC', -system_fee)  # Deduct the system fee from MATIC
            self.matic_fees_paid += system_fee  # Track the total fee paid by the player

            # Add the fee to the system fee deposit
            system_fee_deposit.add_fee(system_fee)

            # Generate a random time and store it
            time_taken = random.randint(0, 300)  # Random time between 0 and 300 seconds

            # Store the time for this map, create a list if it's the player's first time on the map
            if game_map.map_id not in self.times_on_maps:
                self.times_on_maps[game_map.map_id] = []
            self.times_on_maps[game_map.map_id].append(time_taken)  # Add the new time

            # Update the map with the player's time and add XXX to the pool
            game_map.update_player_time(self, time_taken)
            game_map.add_xxx_to_pool(1)
            print(f"{self.name} played on Map {game_map.map_id} and took {time_taken} seconds.")
        else:
            print(f"{self.name} does not have enough XXX tokens or MATIC to play on Map {game_map.map_id}.")

    # def create_map(self, map_registry):
    #     """Create a new map instance and register it, ensuring a unique map ID, and lock NFTs."""
    #     if self.nfts < 1:
    #         print(f"{self.name} does not have enough NFTs to create a map. At least 1 NFT is required.")
    #         return None

    #     # Generate a unique map ID
    #     while True:
    #         map_id = random.randint(1000, 9999)  # Random map ID
    #         if not map_registry.is_map_id_registered(map_id):
    #             break

    #     # Lock a random number of NFTs between 1 and the number of NFTs the player owns
    #     nfts_to_lock = random.randint(1, self.nfts)
    #     self.nfts -= nfts_to_lock  # Deduct locked NFTs from the player's wallet

    #     difficulty = random.choice(["Easy", "Medium", "Hard"])  # Random difficulty
    #     expiration_days = random.randint(7, 30)  # Random expiration days between 7 and 30

    #     new_map = Map(map_id=map_id, difficulty=difficulty, expiration_days=expiration_days,
    #                   creator_id=self.player_id, locked_nfts=nfts_to_lock)

    #     # Register the new map
    #     map_registry.register_map(map_id, self.player_id, datetime.now(), expiration_days, nfts_to_lock)

    #     print(f"{self.name} created Map {map_id} with difficulty '{difficulty}', expiration in {expiration_days} days, "
    #           f"and locked {nfts_to_lock} NFTs.")
    #     return new_map

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

    def mint_nft(self, dev_wallet):
        """Mint an NFT by spending MATIC, transferring the fee to the dev wallet."""
        nft_price = dev_wallet.get_nft_price()

        if self.matic_wallet >= nft_price:
            # Deduct MATIC for minting the NFT
            self.update_wallet('MATIC', -nft_price)
            self.nfts += 1  # Add 1 NFT to player's wallet

            # Add the MATIC to the dev wallet
            dev_wallet.add_matic(nft_price)

            print(f"{self.name} minted an NFT for {nft_price} MATIC.")
        else:
            print(f"{self.name} does not have enough MATIC to mint an NFT.")


class PlayerRegistry:
    def __init__(self):
        self.players = {}  # Dictionary to store player instances by player ID

    def register_player(self, player_id, name, initial_matic):
        """Register a new player and store their instance by player ID."""
        if player_id not in self.players:
            player = Player(player_id, name, initial_matic)
            self.players[player_id] = player
            print(f"Player {name} with ID {player_id} has been registered.")
        else:
            print(f"Player with ID {player_id} already exists.")

    def get_player(self, player_id):
        """Retrieve a player instance by their ID."""
        return self.players.get(player_id, None)

    def __str__(self):
        if not self.players:
            return "No players registered."
        return '\n'.join([str(player) for player in self.players.values()])