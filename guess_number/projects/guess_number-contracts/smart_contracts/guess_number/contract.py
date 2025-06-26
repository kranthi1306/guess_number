from algopy import ARC4Contract, UInt64, Address
from algopy.stdlib import Txn, Global
from algopy.arc4 import arc4
class GuessNumber(ARC4Contract):
    guess_number: UInt64
    winner: Address

    @arc4.abimethod()
    def generated_number(self, hidden_number: UInt64) -> None:
        assert Txn.sender == Global.creator_address(), "Only creator can set number"
        assert hidden_number > UInt64(0), "Number must be positive"
        self.guess_number = hidden_number
        self.winner = Global.zero_address()

    @arc4.abimethod()
    def guess(self, user_guess: UInt64) -> str:
        assert self.winner == Global.zero_address(), "Game already won"
        if user_guess == self.guess_number:
            self.winner = Txn.sender
            return "Correct! You are the winner!"
        elif user_guess < self.guess_number:
            return "Too low!"
        else:
            return "Too high!"

    @arc4.abimethod()
    def get_winner(self) -> Address:
        return self.winner
