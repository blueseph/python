
    ###############################
    #            spells           #
    ###############################

class Spell():
    def __init__(self, name, description, type, base, scaling, cd, priority, range):
        self.name           = name
        self.description    = description
        self.type           = type
        self.base           = base
        self.scaling        = scaling
        self.cd             = cd
        self.priority       = priority
        self.range          = range     #not implemented

    ###############################
    #          spell list         #
    ###############################

spells = {
    #                          description                 type    base    scaling  cd  prior  range
    #                            0                           1       2        3      4    5
           'fireball':  ('casts a fireball at an enemy',  'dmg', (10, 15),   2.5,     6,  9,    0),
      'magic missile':         ('casts a magic missile',  'dmg', (4,  8),    1.3,     0,  5,    0),
               'heal':              ('heals the player', 'heal', (10, 15),     2,    12,  0,    0),
    }

    ###############################
    #       activate spells       #
    ###############################

Fireball        = Spell('fireball', spells['fireball'][0], spells['fireball'][1], spells['fireball'][2], spells['fireball'][3], spells['fireball'][4], spells['fireball'][5], spells['fireball'][6])
Magic_missile   = Spell('magic missile', spells['magic missile'][0], spells['magic missile'][1], spells['magic missile'][2], spells['magic missile'][3], spells['magic missile'][4], spells['magic missile'][5], spells['magic missile'][6])
Heal            = Spell('heal', spells['heal'][0], spells['heal'][1], spells['heal'][2], spells['heal'][3], spells['heal'][4], spells['heal'][5], spells['heal'][6])

    ###############################
    #            buffs            #
    ###############################


class Buff():
    def __init__(self, name, description, target, type, affects, duration, magnitude):
        self.name           = name
        self.description    = description
        self.target         = target
        self.type           = type
        self.affects        = affects
        self.duration       = duration
        self.magnitude      = magnitude

    ###############################
    #        buff list            #
    ###############################

buffs = { 
    #               name                            description                       target     type                 affects          duration                 magnitude    
    #                                                   0                                1         2                      3               4                         5
                 'Bloodlust':                    ('Heals self for small amount',       'self',    'melee',             'curhp',           1,                           10),
                 'Momentum':              ('Next attack will strike critically',       'self',    'melee',              'crit',           2,           (True, True, True)),
                 'Backstab':                   ('Next attack will pierce armor',       'self',    'melee',               'ap',            2,                         True),
                 'Shield Block':       ('Chance to block doubled for next turn',       'self',    'melee',       'blockchance',           2,                            2),
                 'Overcharge':          ('Increases power of next spell by 40%',       'self',    'spell',          'spellmag',           2,                          1.4),

    }
 
    ###############################
    #       activate buffs        #
    ###############################

Buff_bloodlust       = Buff('Bloodlust', buffs['Bloodlust'][0], buffs['Bloodlust'][1], buffs['Bloodlust'][2], buffs['Bloodlust'][3], buffs['Bloodlust'][4], buffs['Bloodlust'][5])
Buff_momentum        = Buff('Momentum', buffs['Momentum'][0], buffs['Momentum'][1], buffs['Momentum'][2], buffs['Momentum'][3], buffs['Momentum'][4], buffs['Momentum'][5])
Buff_backstab        = Buff('Backstab', buffs['Backstab'][0], buffs['Backstab'][1], buffs['Backstab'][2], buffs['Backstab'][3], buffs['Backstab'][4], buffs['Backstab'][5])
Buff_shield_block    = Buff('Shield Block', buffs['Shield Block'][0], buffs['Shield Block'][1], buffs['Shield Block'][2], buffs['Shield Block'][3], buffs['Shield Block'][4], buffs['Shield Block'][5])
Buff_overcharge      = Buff('Overcharge', buffs['Overcharge'][0], buffs['Overcharge'][1], buffs['Overcharge'][2], buffs['Overcharge'][3], buffs['Overcharge'][4], buffs['Overcharge'][5])
    

    ###############################
    #          abilities          #
    ###############################

class Ability():
    def __init__(self, name, description, occurance, effect, affects, magnitude, buffplaced):
        self.name           = name
        self.description    = description
        self.occurance      = occurance
        self.effect         = effect
        self.affects        = affects
        self.magnitude      = magnitude
        self.cooldown       = cooldown
        self.buffplaced     = buffplaced

    ###############################
    #       abilities list        #
    ###############################

abilities = {
    #               name                            description                  occurs         target       affects      magnitude    cooldown
    #                                                   0                           1              2            3            4             5            
'berserker': {
              'Bloodlust':                       ('Heals for a small amount', 'deathblow',       'heal',     'curhp',         .2,          0,       Buff_bloodlust),
        'Overhead Strike':           ('Strikes the target with medium force',    'active',        'dmg',    'weapon',        1.5,          3,                 None),
    },

'rogue': {
               'Momentum': ('Next attack is guaranteed to strike critically', 'deathblow',       'dmg',      'crit',        100,          0,         Buff_momentum),
               'Backstab':        (    'Attacks from behind, piercing armor',    'active',       'dmg',        'ac',        200,          6,         Buff_backstab),
    },

'warrior': {
            'Shield Slam':                         ('Returns blocked damage',     'active',      'dmg', 'blockdmg',          1,          2,                  None),
           'Shield Block':          ('Chance to block doubled for next turn',  'deathblow',     'buff', 'blockval',          2,          0,     Buff_shield_block),
    },

'wizard': {
            'Overcharge':            ('Increases power of next spell by 40%',     'active',     'buff', 'spellmag',        .4,          4,        Buff_overcharge),

    }
}

    
    ###############################
    #     activate abilities      #
    ###############################

