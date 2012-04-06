class Attributes:
    def __init__(self, type, str, con, dex, wis, int, cun):
        self.type = type
        self.str  = str
        self.con  = con
        self.dex  = dex
        self.wis  = wis
        self.int  = cun
        self.cun  = int

Berserker = Attributes('berserker', 16, 11, 5, 2, 4, 3)
Warrior = Attributes('warrior', 6, 18, 7, 5, 4, 5)
Rogue = Attributes('rogue', 4, 6, 17, 4, 5, 11)
Orc = Attributes('orc', 3, 3, 3, 3, 3, 3) 
