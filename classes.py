class Attributes:
    def __init__(self, str, con, dex, wis, int, cun):
        self.str = str
        self.con = con
        self.dex = dex
        self.wis = wis
        self.int = cun
        self.cun = int

Berserker = Attributes(16, 11, 5, 2, 4, 3)
Warrior = Attributes(6, 18, 7, 5, 4, 5)
Assassin = Attributes(4, 5, 8, 4, 5, 12)
Rogue = Attributes(4, 6, 17, 4, 5, 11)
Orc = Attributes(3, 3, 3, 3, 3, 3) 
