from algopy import ARC4Contract, arc4, Txn, Global

class GuessNumber(ARC4Contract):
    guess_number: arc4.UInt64
    winner: arc4.Address  # Use Address type for compatibility

    @arc4.abimethod()
    def generated_number(self, hidden_number: arc4.UInt64) -> None:
        assert Txn.sender == Global.creator_address, "Only creator can set number"
        assert hidden_number > arc4.UInt64(0), "Number must be positive"
        self.guess_number = hidden_number
        self.winner = arc4.Address(Global.zero_address)  # Properly assign zero address

    @arc4.abimethod()
    def guess(self, user_guess: arc4.UInt64) -> arc4.String:
        assert self.winner ==arc4.Address(Global.zero_address), "Game already won"
        if user_guess == self.guess_number:
            self.winner = arc4.Address(Txn.sender)  # Convert sender to Address
            return arc4.String("Correct! You are the winner!")
        elif user_guess < self.guess_number:
            return arc4.String("Too low!")
        else:
            return arc4.String("Too high!")

    @arc4.abimethod()
    def get_winner(self) -> arc4.Address:
        return self.winner