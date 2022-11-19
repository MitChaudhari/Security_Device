from SecurityEngine import *
import time
import sys
from test.sortperf import flush
import math

class ranNumGen:
    def __init__(self):
        self.listOfNums = []
        self.listOfNums2 = []

        
        
    
    def bruteForce(self):
        bruteForce = SecurityEngine()
        NumSysmGen = 0
        for i in range(10):
            while bruteForce.UnLock != True:
                n = random.randint(0,1000000000) # This will generate a random num between 0 and 1 billion
                bruteForce.setData(str(n))
                bruteForce.currentState()
                NumSysmGen+=1
            self.listOfNums.append(NumSysmGen)
            bruteForce.UnLock = False
        self.listOfNums.sort()
        print(self.listOfNums)
        
    def resultsCheck(self):
        max_value = max(self.listOfNums)
        min_value = min(self.listOfNums)
        avg_value = 0 if len(self.listOfNums) == 0 else sum(self.listOfNums)/len(self.listOfNums)
        print("The Minimum tries to Unlock: " + str(min_value)+"\n" 
              + "The Maximum tries to Unlock: " + str(max_value)+"\n"
              + "The Average tries to Unlock " + str(avg_value))
        
            
    def waitAndCheck(self):
        
        bruteForce = SecurityEngine()
        NumSysmGen = 0
        listempyString = []
        for i in range(3):
            start = time.time()
            while bruteForce.UnLock != True:
                n = random.randint(0,1000000000) # This will generate a random num between 0 and 1 billion
                bruteForce.setData(str(n))
                bruteForce.currentState()
                time.sleep(1)
            bruteForce.UnLock = False
            end = time.time()
            total_time = (math.trunc((end-start)))
            self.listOfNums2.append(total_time)
        
        
        self.listOfNums2.sort()
        print(self.listOfNums2)
        avg_value = 0 if len(self.listOfNums2) == 0 else sum(self.listOfNums2)/len(self.listOfNums2)
        print("The Average tries to Unlock " + str(avg_value) +"seconds")
        
      

    
        

        
        
        
        
        
        
        
        
########################################################################################################################
######################################                                      ############################################
######################################     Testing     the code             ############################################
######################################                                      ############################################
########################################################################################################################
# testRanGen = ranNumGen()
# # testRanGen.bruteForce()
# # testRanGen.resultsCheck()
# testRanGen.waitAndCheck()



