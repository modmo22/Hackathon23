from Mobs.bat import Bat
from Mobs.aligator import Aligator
from Mobs.snek import Snek
from Stages.Level1 import Level1
from Stages.Level2 import Level2
from Stages.Level3 import Level3

class Springboard():
    def __init__(self):
        print(__file__)

    def importTest(self):
        print("Testing")
        l1 = Level1()
        l2 = Level2()
        l3 = Level3()
        b = Bat()
        a = Aligator()
        s = Snek()
