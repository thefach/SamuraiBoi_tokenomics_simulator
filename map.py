class Map:
    def __init__(self, map_id, difficulty):
        self.map_id = map_id
        self.difficulty = difficulty  # Could be a factor affecting time or reward
        self.player_times = {}  # Dictionary to store {player_id: best_time}
        self.best_time = None  # Overall best time on the map
        self.best_player = None  # Player with the overall best time
        self.xxx_pool = 0  # Total XXX tokens accumulated for the map

    def __str__(self):
        """Display map details."""
        player_times_str = ', '.join([f"Player {pid}: {time}" for pid, time in self.player_times.items()]) or 'No players yet'
        return (f"Map {self.map_id}:\n"
                f"  Difficulty: {self.difficulty}\n"
                f"  Player Times: {player_times_str}\n"
                f"  Best Time: {self.best_time if self.best_time else 'No best time yet'}\n"
                f"  Best Player: {self.best_player if self.best_player else 'No best player yet'}\n"
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
            self.best_player = player.name
            print(f"New overall best time on Map {self.map_id}: {time_taken} seconds by {player.name}.")

    def add_xxx_to_pool(self, amount):
        """Add XXX tokens to the map's pool when a player plays."""
        self.xxx_pool += amount
        print(f"Map {self.map_id} now has {self.xxx_pool} XXX tokens in the pool.")
