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
        kill_count = 0
        combat.fight()                                  

        while gameturn.playerDeath is False:
            kill_count += 1
            classes.chooseMonsterClass()        #rerolls monster
            combat.fight()          #fights again

        if kill_count is 1:
                print('You have died. You killed %s monster.' % kill_count)
        else:
        	print('You have died. You killed %s monsters.' % kill_count)
        time.sleep(10)
