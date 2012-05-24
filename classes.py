import equipment
import itemlist
import random
import levelingstats
import gameturn
import combat
import combatdisplay
import spells
import stringparse
from operator import itemgetter
from constants import *

creatures = {}

class Attributes:
    def __init__(self, unitclass, str, con, dex, wis, int, cun, curlvl, display):
        self.unitclass  = unitclass
        self.str        = str
        self.con        = con
        self.dex        = dex
        self.wis        = wis
        self.int        = int
        self.cun        = cun
        self.curlvl     = curlvl
        self.display    = display

class Creature(Attributes):
    
    ###############################
    #       sets initial stats    #
    ###############################

    def recordStats(self):
        self.currentStats = {
        'str': self.str,
        'con': self.con,
        'dex': self.dex,
        'wis': self.wis,
        'int': self.int,
        'cun': self.cun
        }

    def resetStats(self):
        self.str = self.currentStats['str']
        self.con = self.currentStats['con']
        self.dex = self.currentStats['dex']
        self.wis = self.currentStats['wis']
        self.int = self.currentStats['int']
        self.cun = self.currentStats['cun']

    def calculateStats(self):
        self.maxhp      = self.con * CONSTITUTION_MULT
        if self.dex > self.str:
            self.dmg    = int(self.dex//WEP_DEX_BONUS)
        else:
            self.dmg    = int(self.str//WEP_STR_BONUS)
        self.recordStats()
    
    def __init__(self, Attributes):
        self.display            = Attributes.display
        self.unitclass          = Attributes.unitclass
        self.str                = Attributes.str
        self.con                = Attributes.con
        self.dex                = Attributes.dex
        self.wis                = Attributes.wis
        self.int                = Attributes.int
        self.cun                = Attributes.cun
        self.curlvl             = Attributes.curlvl
        self.type               = 'monster'
        if self.unitclass is 'wizard':
            self.atype          = 'magic'
        else:
            self.atype          = 'melee'
        self.calculateStats()
        self.curhp              = self.maxhp
        self.xPos               = 10
        self.yPos               = 10
        self.mainhand           = None
        self.offhand            = None
        self.offhandWeight      = 0
        self.armorWeight        = 0
        self.inventory          = []
        self.spells             = []
        self.spellCooldowns     = {}
        self.healSpells         = []
        self.dmgSpells          = []
        self.activeBuffs        = []
        self.buffDuration       = {}
        self.initBuffs          = []
        self.midBuffs           = []
        self.endBuffs           = []
        self.abilities          = []
        self.dmgAbilities       = []
        self.healAbilities      = []
        self.abilityCooldowns   = {}
        self.preRollStats       = {
        'unitclass': self.unitclass,
        'str': self.str,
        'con': self.con,
        'dex': self.dex,
        'wis': self.wis,
        'int': self.int,
        'cun': self.cun
        }

    ###############################
    #       equipment system      #
    ###############################

    def equip(self, item):
        if (item.type is '1h' or '2h') and (self.mainhand is None): #deletes currently equipped items. need to fix
            self.mainhand           = item.type
            self.mainhandWeaponName = item.name
            self.mainhandWeight     = item.weight
            self.mainhandGoldValue  = item.goldValue
            self.mainhandWepMin     = item.wepMin
            self.mainhandWepMax     = item.wepMax
            self.mainhandCrit       = item.wepCrit
            self.mainhandCritDmg    = item.wepCritDmg
            self.mainhandRange      = item.wepRange # need to impliment range
        elif self.mainhand is '1h' and item.type is '1h':
            self.offhand            = item.type
            self.offhandItemName    = item.name
            self.offhandWeight      = item.weight
            self.offhandGoldValue   = item.goldValue
            self.offhandWepMin      = item.wepMin
            self.offhandWepMax      = item.wepMax
            self.offhandCrit        = item.wepCrit
            self.offhandCritDmg     = item.wepCritDmg
            self.offhandRange       = item.wepRange
        elif item.type is 'shield':
            self.offhand            = item.type
            self.offhandItemName    = item.name
            self.offhandWeight      = item.weight
            self.offhandGoldValue   = item.goldValue
            self.offhandBlockValue  = item.blockValue
            self.offhandBlockChance = item.blockChance
        elif (item.type is not 'shield' or '1h' or '2h'):
            self.armorName          = item.name
            self.armorWeight        = item.weight
            self.armorGoldValue     = item.goldValue
            self.armorClass         = item.armorClass
        self.weight = self.mainhandWeight + self.offhandWeight + self.armorWeight

    ###############################
    #       inventory system      #
    ###############################

    def addInventoryItem(self, item): 
        self.inventory.append(item)

    ###############################
    #          xp system          #
    ###############################
    
    def giveXP(self):
        return int(10 + (self.curlvl ** 3.05))
        #int(random.randint((i+5), (i+8)) + (((i+2) ** 4)/6))

    ###############################
    #       spell system          #
    ###############################

    def getSpell(self, spell):
        self.spells.append(spell)
        if spell.type is 'heal':
            self.healSpells.append(spell)
        if spell.type is 'dmg':
            self.dmgSpells.append(spell)

    # automated spellcast system

    def determineAvgMag(self, spell):
        return ((spell.base[0]+spell.base[1])/2 + (self.int * spell.scaling))

    def shouldUseHeal(self):
        useHeal = False
        healSpell = None
        avgHeal = 0
        try:
            for heal in self.healSpells:
                if self.determineAvgMag(heal) > avgHeal:
                    healSpell = heal
                    avgHeal = self.determineAvgMag(heal)
            if self.curhp < (self.maxhp - avgHeal):
                useHeal = True
        except NameError:
            healSpell = None
            useHeal = False
        return useHeal, healSpell

    def getSpellAvail(self, spell):
        try:
            if self.spellCooldowns[spell.name] is not 0:
                return False
            else:
                return True
        except:
            return True

    def getSpellToCast(self):
        spellToCast = ''
        shouldUseHeal = self.shouldUseHeal()
        if shouldUseHeal[0] is True:
            spellToCast = shouldUseHeal[1]
        if shouldUseHeal[0] is False:
            spellPriority = []
            for spell in self.dmgSpells:
                spellPriority.append((spell, spell.priority))
            spellPriority = sorted(spellPriority, key=itemgetter(1), reverse=True)
            for spell in range(len(spellPriority)):
                if self.getSpellAvail(spellPriority[spell][0]) is True:
                    spellToCast = spellPriority[spell][0]
                    break
                else:
                    pass
        return spellToCast
            
    def cast(self, spell, target):
        if spell in self.dmgSpells:
            spellMag = int(random.randint(spell.base[0], spell.base[1]) + (self.int * spell.scaling))
            target.curhp -= spellMag
            combat.determineDeath(target)
        elif spell in self.healSpells:
            spellMag = int(random.randint(spell.base[0], spell.base[1]) + (self.int * spell.scaling))
            self.curhp += spellMag
            if self.curhp > self.maxhp:
                self.curhp = self.maxhp
        combatdisplay.inCombatScreen(stringparse.castStringParse(self, target, spell, spellMag), 1.5)
        self.spellCooldowns[spell.name] = spell.cd

    ###############################
    #       melee system          #
    ###############################

    #system needs cleanup

    def dmgRoll(self):
        wepOhDmg = 0
        wepMhDmg = random.randint(self.mainhandWepMin, self.mainhandWepMax) + self.dmg
        if self.offhand is not None and self.offhand is not 'shield':
            wepOhDmg = (random.randint(self.offhandWepMin, self.offhandWepMax) + self.dmg)/2
        return wepMhDmg, wepOhDmg

    def critRoll(self):
        critRoll, unitOffhandCrit, unitMainhandCrit = False, False, False
        unitCritMod = int(self.dex/3)
        if random.randint(1, 20) <= (unitCritMod + self.mainhandCrit):
            unitMainhandCrit = True
        if self.offhand is not None and self.offhand is not 'shield':
            if (random.randint(1, 20) <= (unitCritMod + self.offhanddCrit)):
                unitoffhandCrit = True
        if unitMainhandCrit is True or unitOffhandCrit is True:
            critRoll is True
        return critRoll, unitOffhandCrit, unitMainhandCrit

    def armorpierceRoll(self):
        apRoll = False
        if (random.randint(1, 20) <= int(self.cun/2)):
            apRoll = True
        return apRoll

    def blockRoll(self, target):
        blockRoll = False
        if target.offhand is 'shield':
            if (random.randint(1, 10) <= target.offhandBlockChance):
                blockRoll = True
        return blockRoll

    def melee(self, target):
        offhand = None
        if self.offhand is not None:
            offhand = self.offhand
        self.initBuff()
        wepMhDmg, wepOhDmg = self.dmgRoll()
        critRoll = self.critRoll()
        apRoll = self.armorpierceRoll()
        blockRoll = self.blockRoll(target)
        self.midBuff(critRoll, apRoll, blockRoll)
        if blockRoll is True:
            wepMhDmg -= target.offhandBlockValue
            wepOhDmg -= target.offhandBlockValue
        if critRoll[0] is True:
            if critRoll[1] is True:
                wepMhDmg *= self.mainhandCrit
            elif critRoll[2] is True:
                wepOhDmg *= self.offhandCrit
        if wepOhDmg < 0:
            wepOhDmg = 0
        wepTotDmg = int(wepMhDmg) + int(wepOhDmg)
        if wepTotDmg < 0:
            wepTotDmg = 0
        self.endBuff(wepTotDmg)
        target.curhp -= wepTotDmg
        combat.determineDeath(target)

    ###############################
    #       buffs system          #
    ###############################

    def populatePostRollStats(self, critRoll, apRoll, blockRoll):
        self.postRollStats      = {
        'crit': critRoll,
        'ap': apRoll,
        'block': blockRoll
        }

    def populateEndRollStats(self, wepTotDmg):
        self.endRollStats       = {
        'wepdmg': wepTotDmg
        }

    def initBuff(self):
        if len(self.initBuffs) > 0:
            for buff in self.initBuffs:
                self.preRollStats[buff] = buff.magnitude
                self.buffDuration['buff.name'] = buff.duration
        pass

    def midBuff(self, critRoll, apRoll, blockRoll):
        self.populatePostRollStats(critRoll, apRoll, blockRoll)
        if len(self.midBuffs) > 0:
            for buff in self.midBuffs:
                self.postRollStats[buff] = buff.magnitude
                self.buffDuration['buff.name'] = buff.duration
        pass

    def endBuff(self, wepTotDmg):
        self.populateEndRollStats(wepTotDmg)
        if len(self.endBuffs) > 0:
            for buff in self.endBuffs:
                self.endRollStats[buff] = buff.magnitude
                self.buffDuration['buff.name'] = buff.duration

    ###############################
    #       ability system        #
    ###############################

    def getAbility(self, ability):
        self.abilities.append(ability)
        if ability.type is 'dmg':
            self.dmgAbilities.append(ability)
        if ability.type is 'heal':
            self.healAbilities.append(ability)

    def useAbility(self, ability):
        if ability in self.dmgAbilities:
            pass

    ###############################
    #       movement system       #
    ###############################

    def setInitSpawn(self):
        self.xPos = random.randint(8, BOARD_WIDTH - 10)
        self.yPos = random.randint(4, BOARD_HEIGHT - 6)

    def collisionCheck(self, dx, dy):
        for creature in creatures:
            if creatures[creature] is self:
                pass
            elif self.xPos + dx is creatures[creature].xPos and self.yPos + dy is creatures[creature].yPos:
                return True, creatures[creature]
                print(creatures[creature])
                break
        return False, None

    def move(self, dx, dy): # delta x and y
        collide, target = self.collisionCheck(dx, dy)
        if collide is True:
            self.melee(target)
        else:
            self.xPos += dx
            self.yPos += dy
        
class Player(Creature): 
    def __init__(self, Creature):
        self.display            = '@'
        self.unitclass          = Creature.unitclass
        self.str                = Creature.str
        self.type               = 'player'
        self.con                = Creature.con
        self.dex                = Creature.dex
        self.wis                = Creature.wis
        self.int                = Creature.int
        self.cun                = Creature.cun
        self.curlvl             = Creature.curlvl
        if self.curlvl is 1:
            self.curXP          = 0
        else:
            self.curXP          = levelingstats.xpToLevel[self.curLvl - 1]
        self.calculateStats()
        self.curhp              = self.maxhp
        self.xPos               = 9
        self.yPos               = 10
        self.mainhand           = None
        self.offhand            = None
        self.offhandWeight      = 0
        self.armorWeight        = 0
        self.inventory          = []
        self.spells             = []
        self.spellCooldowns     = {}
        self.healSpells         = []
        self.dmgSpells          = []
        self.activeBuffs        = []
        self.buffDuration       = {}
        self.initBuffs          = []
        self.midBuffs           = []
        self.endBuffs           = []
        self.abilities          = []
        self.dmgAbilities       = []
        self.healAbilities      = []
        self.abilityCooldowns   = {}
        self.preRollStats       = {
        'unitclass': self.unitclass,
        'str': self.str,
        'con': self.con,
        'dex': self.dex,
        'wis': self.wis,
        'int': self.int,
        'cun': self.cun,
        'curhp': self.curhp}

    ###############################
    #     player xp system        #
    ###############################
    
    def gainXP(self, xp):
        self.curXP += xp
        if self.curXP > levelingstats.xpToLevel[self.curlvl + 1]:
            gameturn.unitGainLvl = True

def chooseClass():
    print('Choose your class')
    print(' ')
    print('''B: Berserker (STR, CON)
R: Rogue (DEX, CUN)
W: Warrior (CON, STR)
w: Wizard (INT, WIS)
''')
    playerClass = None
    while playerClass is None:
        playerClass = input()
        if playerClass.startswith('W'):
            playerClass         = Warrior
            weapon          = equipment.Weapon(*equipment.chooseWeapon(itemlist.weapon_list, 0))
            armor           = equipment.Armor(*equipment.chooseArmor(itemlist.armor_list, 4))
            offhand         = equipment.Shield(*equipment.chooseShield(itemlist.shield_list, 1))
            hasOffhand      = True
        elif playerClass.startswith('B'):
            playerClass = Berserker
            weapon          = equipment.Weapon(*equipment.chooseWeapon(itemlist.weapon_list, 5))
            armor           = equipment.Armor(*equipment.chooseArmor(itemlist.armor_list, 2))
            hasOffhand      = False
        elif playerClass.startswith('R'):
            playerClass = Rogue
            weapon          = equipment.Weapon(*equipment.chooseWeapon(itemlist.weapon_list, 3))
            offhand         = equipment.Weapon(*equipment.chooseWeapon(itemlist.weapon_list, 3))
            armor           = equipment.Armor(*equipment.chooseArmor(itemlist.armor_list, 1))
            hasOffhand = True
        elif playerClass.startswith('w'):
            playerClass = Wizard
            weapon          = equipment.Weapon(*equipment.chooseWeapon(itemlist.weapon_list, 8))
            armor           = equipment.Armor(*equipment.chooseArmor(itemlist.armor_list, 0))
            hasOffhand = False
        else:
            playerClass = None
            print('Choose your class')
            print(' ')
            print('''B: Berserker (STR, CON)
R: Rogue (DEX, CUN)
W: Warrior (CON, STR)
w: Wizard (INT, WIS)
''')
            print('Please choose a valid response')
    player = Player(Creature(playerClass))
    player.addInventoryItem(weapon)
    player.addInventoryItem(armor)
    player.equip(weapon) 
    player.equip(armor)
    if hasOffhand is True:
        player.equip(offhand)
        player.addInventoryItem(offhand)
    if player.unitclass is 'wizard':
        player.getSpell(spells.Fireball)
        player.getSpell(spells.Magic_missile)
        player.getSpell(spells.Heal)
    player.setInitSpawn()
    creatures['player'] = player

def chooseMonsterClass():
    monsterClass = Orc
    monster = Creature(monsterClass)
    weapon = equipment.Weapon(*equipment.chooseWeapon(itemlist.weapon_list, random.randint(0, 7)))
    armor  = equipment.Armor(*equipment.chooseArmor(itemlist.armor_list, random.randint(0, 5)))
    monster.addInventoryItem(weapon)
    monster.addInventoryItem(armor)
    monster.equip(weapon)
    monster.equip(armor)
    monster.setInitSpawn()
    creatures['monster'] = monster
    
#                                  st co de wi in cu lvl disp
Berserker = Attributes('berserker', 7, 5, 3, 3, 4, 3, 1, '@')
Warrior     = Attributes('warrior', 4, 7, 3, 3, 3, 5, 1, '@')
Rogue         = Attributes('rogue', 3, 4, 7, 4, 5, 6, 1, '@')
Wizard       = Attributes('wizard', 2, 3, 3, 6, 8, 2, 1, '@')
Orc             = Attributes('orc', 2, 2, 2, 2, 2, 2, 1, 'o') 
