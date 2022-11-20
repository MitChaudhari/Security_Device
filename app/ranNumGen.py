from SecurityEngine import *
import time
import sys
import math

class ranNumGen:
    def __init__(self):
        self.listOfNums = []
        self.listOfNums2 = []
        self.max_value = 0
        self. min_value = 0
        self.avg_value = 0 
    
    def bruteForce(self, trials = None):
        if trials == None or trials <=1:
            trials = 5  #By Defualt run the program 5 times to get the Average
            
        bruteForce = SecurityEngine()
        NumSysmGen = 0
        for i in range(trials):
            while bruteForce.main_unlock != True:
                n = random.randint(0,1000000000) # This will generate a random num between 0 and 1 Billion 
                bruteForce.setData(str(n))
                bruteForce.currentState()
                NumSysmGen+=1
            self.listOfNums.append(NumSysmGen)
            bruteForce.main_unlock = False
        self.listOfNums.sort()
        return(self.listOfNums)
        
    def resultsCheck(self):
        self.max_value = max(self.listOfNums)
        self.min_value = min(self.listOfNums)
        self.avg_value = 0 if len(self.listOfNums) == 0 else sum(self.listOfNums)/len(self.listOfNums)
        return("The Minimum tries to Unlock: " + str(self.min_value)+"\n" 
              + "The Maximum tries to Unlock: " + str(self.max_value)+"\n"
              + "The Average tries to Unlock " + str(self.avg_value))
        
            
    def WaitAndCheck(self):
        
        bruteForce = SecurityEngine()
        NumSysmGen = 0
        for i in range(3):
            start = time.time()
            while bruteForce.main_unlock != True:
                n = random.randint(0,1000000000000) # This will generate a random num between 0 and 1 billion
                bruteForce.setData(str(n))
                bruteForce.currentState()
                time.sleep(1)
            bruteForce.main_unlock = False
            end = time.time()
            total_time = (math.trunc((end-start)))
            self.listOfNums2.append(total_time)
        
        self.listOfNums2.sort()
        print(self.listOfNums2)
        self.avg_value = 0 if len(self.listOfNums2) == 0 else sum(self.listOfNums2)/len(self.listOfNums2)
        self.avg_value=(math.trunc(self.avg_value))
        return("The Average tries to Unlock " + str(self.avg_value) +" seconds")
        
      

    
        

        
        
        
        
        
        
        
        
########################################################################################################################
######################################                                      ############################################
######################################     Testing     the code             ############################################
######################################                                      ############################################
########################################################################################################################
# testRanGen = ranNumGen()
# print(testRanGen.bruteForce())
# print(testRanGen.resultsCheck())
# testRanGen.WaitAndCheck()





