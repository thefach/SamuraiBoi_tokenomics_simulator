from datetime import datetime, timedelta

class Map:
    def __init__(self, map_id, difficulty, expiration_days, creator_id, locked_nfts):
        self.map_id = map_id
        self.difficulty = difficulty  # Difficulty level of the map
        self.creator_id = creator_id  # Player ID of the creator
        self.expiration_days = expiration_days  # Number of days until map expires
        self.locked_nfts = locked_nfts  # Number of NFTs locked in the map by the creator
        self.creation_date = datetime.now()  # Date the map was created
        self.player_times = {}  # Dictionary to store {player_id: best_time}
        self.best_time = None  # Overall best time on the map
        self.best_player_id = None  # Player ID with the overall best time
        self.xxx_pool = 0  # Total XXX tokens accumulated for the map

    def __str__(self):
        """Display map details."""
        player_times_str = ', '.join([f"Player {pid}: {time}" for pid, time in self.player_times.items()]) or 'No players yet'
        return (f"Map {self.map_id}:\n"
                f"  Created by Player ID: {self.creator_id}\n"
                f"  Difficulty: {self.difficulty}\n"
                f"  Expiration Days: {self.expiration_days}\n"
                f"  Locked NFTs: {self.locked_nfts}\n"
                f"  Player Times: {player_times_str}\n"
                f"  Best Time: {self.best_time if self.best_time else 'No best time yet'}\n"
                f"  Best Player ID: {self.best_player_id if self.best_player_id else 'No best player yet'}\n"
                f"  XXX Pool: {self.xxx_pool} tokens")

    def update_player_time(self, player, time_taken):
        """Update the best time for a specific player on this map."""
        player_id = player.player_id
        if player_id not in self.player_times or time_taken < self.player_times[player_id]:
            self.player_times[player_id] = time_taken  # Update the best time for this player
            print(f"{player.name} completed Map {self.map_id} in {time_taken} seconds.")
        
        self.update_best_time(player, time_taken)

    def update_best_time(self, player, time_taken):
        """Update the overall best time on the map."""
        if self.best_time is None or time_taken < self.best_time:
            self.best_time = time_taken
            self.best_player_id = player.player_id
            print(f"New overall best time on Map {self.map_id}: {time_taken} seconds by {player.name}.")

    def add_xxx_to_pool(self, amount):
        """Add XXX tokens to the map's pool when a player plays."""
        self.xxx_pool += amount
        print(f"Map {self.map_id} now has {self.xxx_pool} XXX tokens in the pool.")

    def get_creator_id(self):
        """Return the creator ID of the map."""
        return self.creator_id

    def get_best_player_id(self):
        """Return the best player ID of the map."""
        return self.best_player_id

    def map_expired(self, player_registry):
        """Check if the map has expired and distribute rewards if it has."""
        expiration_date = self.creation_date + timedelta(days=self.expiration_days)
        if datetime.now() >= expiration_date:
            # Map has expired, distribute rewards
            if self.best_player_id is not None:
                best_player = self.best_player_id 
                # Give NFTs to the best player
                player_registry.get_player(best_player).nfts += self.locked_nfts
                print(f"Player {player_registry.get_player(best_player).name} received {self.locked_nfts} NFTs from Map {self.map_id}.")

                # Give 20% of XXX to the best player and 80% to the creator
                xxx_for_best_player = int(self.xxx_pool * 0.2)
                xxx_for_creator = self.xxx_pool - xxx_for_best_player

                player_registry.get_player(best_player).update_wallet('XXX', xxx_for_best_player)
                print(f"Player {player_registry.get_player(best_player).name} received {xxx_for_best_player} XXX tokens from Map {self.map_id}.")

                # Get the creator player instance to update their balance
                creator_player = self.creator_id
                player_registry.get_player(creator_player).update_wallet('XXX', xxx_for_creator)
                print(f"Player {player_registry.get_player(creator_player)} received {xxx_for_creator} XXX tokens from Map {self.map_id}.")

            else:
                print(f"Map {self.map_id} expired but no player participated.")

            # Clear the map state after expiration
            self.locked_nfts = 0
            self.xxx_pool = 0

            return True  # Indicate that the map has expired and actions were taken
        else:
            return False  # The map has not expired yet


class MapRegistry:
    def __init__(self):
        self.maps = {}  # Dictionary to store map instances by map ID

    def register_map(self, map_id, difficulty, expiration_days, creator_id, locked_nfts):
        """Register a new map and store its instance by map ID."""
        if map_id not in self.maps:
            map_instance = Map(map_id, difficulty, expiration_days, creator_id, locked_nfts)
            self.maps[map_id] = map_instance
            print(f"Map with ID {map_id} has been registered.")
        else:
            print(f"Map with ID {map_id} already exists.")

    def get_map(self, map_id):
        """Retrieve a map instance by its ID."""
        return self.maps.get(map_id, None)
    
    def is_map_id_registered(self, map_id):
        """Check if a map ID is already registered."""
        return any(map_record['map_id'] == map_id for map_record in self.maps)

    def __str__(self):
        if not self.maps:
            return "No maps registered."
        return '\n'.join([str(map_instance) for map_instance in self.maps.values()])

    def check_expired_maps(self, player_registry):
        """Check all maps in the registry and perform expiration actions if needed."""
        maps = self.maps
        print(maps)
        for game_map in maps:
            print(game_map)
            print(self.get_map(game_map))
            #creator_id, best_player_id = game_map.creator_id, game_map.best_player_id
            if self.get_map(game_map).map_expired(player_registry):
                print(f"Map {self.get_map(game_map).map_id} has expired and rewards have been distributed.")


    

