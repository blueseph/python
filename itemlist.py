#IMPORTANT NEED TO ADD TYPE OF VERBS TO THE TABLE

weapon_list = [ 
#item name, gold value, min dmg, max dmg, crit rate, crit dmg,  attack range, weight, verbs]
#		0		 1   2   3   4    5    6    7    8
	[ "longsword", 		15, 10, 14,   1, 1.5,  1,  40, '1h'],   # 0
	[ "shortsword", 	10,  8, 11, 1.5, 2.0,  1,  30, '1h'],   # 1
	[ "greatsword",		25, 18, 22,   1, 1.5,  1,  80, '2h'],   # 2  
	[ "dagger",		7,   4,  7,   3, 3.0,  1,   9, '1h'],   # 3
	[ "hand axe",		15,  9, 10,   2, 2.5,  1,  50, '1h'],   # 4
	[ "greataxe",		30, 19, 20,   2, 2.5,  1,  85, '2h'],   # 5
	[ "mace",		15, 14, 16, .10,   6,  1,  55, '1h'],   # 6
	[ "warhammer",		35, 24, 26, .10,   6,  1,  95, '2h'],   # 7
        [ "worn staff",         15,  6, 10,   0,   0,  1,  35, '2h'],   # 8

]
 
armor_list = [
       # item name, gold value, ac, weight
	[ "cloth",		8,    0,   1, 'chest'], #0
	[ "leather",		15,   2,  25, 'chest'], #1
	[ "chain shirt",	80,   4,  70, 'chest'], #2
	[ "chainmail",		150,  5,  90, 'chest'], #3
	[ "splintmail",		245,  8, 110, 'chest'], #4
	[ "plate mail",		450, 12, 130, 'chest'], #5
]

shield_list = [
    #item name, gold value, block value, weight, type
    [ "small shield",           8,  2,  20, 'shield'], #0
    [ "round shield",          15,  4,  35, 'shield'], #1 
    [ "kite shield",           40,  6,  50, 'shield'], #2
    [ "tower shield",          70,  9,  80, 'shield'], #3
    ]
