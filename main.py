import combat
import equipment
import classes
import time
import gameturn

    ###############################
    #   chooses class and fights  #
    ###############################
    
if __name__ == "__main__":
        classes.chooseClass()                           
        classes.chooseMonsterClass()
        combat.fight()                                  

        while gameturn.playerDeath is False:
            classes.chooseMonsterClass()        #rerolls monster
            combat.fight()          #fights again

        time.sleep(5)
