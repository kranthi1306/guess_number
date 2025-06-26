from algopy import *
class guess_number(ARC4Contract)
  class global_state(globalState)
    guess_number=UInt8   
@Arc4.abimethod()
def random_number(self,guess:UInt8)->none:
  