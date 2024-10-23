class SystemFeeDeposit:
    def __init__(self):
        self.total_fees = 0  # Total MATIC fees accumulated from all players
        self.system_fee = 0.0005  # Fee amount for each play action in MATIC

    def add_fee(self, fee):
        """Add the fee collected from a player to the total fees."""
        self.total_fees += fee

    def get_fee(self):
        """Get the system fee amount."""
        return self.system_fee

    def __str__(self):
        """Define how to print the total fees accumulated."""
        return f"Total MATIC Fees in System: {self.total_fees}"
