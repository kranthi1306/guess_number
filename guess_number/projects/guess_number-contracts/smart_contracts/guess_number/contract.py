from algopy import *
class guess_number(ARC4Contract)
  class local_state(LocalState)
    guess_number=UInt8   
 @Arc4.abimethod()
 def random_number(self,guess:UInt8)->UInt8:
