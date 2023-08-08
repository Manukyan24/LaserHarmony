import random
import time
#cash = {"num": None}
a=1
def signal_emulator():

    print(random.randint(0, 127))
    #time.sleep(2)
    global a 
    a = random.randint(0, 127)
    signal_emulator()
    



#this may be useful, but we are not gonna use it(maybe)
    #if google == 10:
    #    return 0
    #else:
    #    cash["num"] = random.randint(0, 127)
    #    print(cash)
    #    signal_emulator(google+1)

#cash = {"num": None}
#def signal_emulator(google = 0):
#    cash["num"] = random.randint(0, 127)
#    print(cash)
#    signal_emulator(google+1)
#    if google == 10:
#        return 0
#
#signal_emulator()
