# CS330 A security Device Assignment Version 1, 11/15/2022
# Created By: Mitansh Chaudahri 

# This class will implement Random number generation for the Security Engine.  
# That will unlock the lock when it finds the 
# correct un-locking access and lock when it finds 
# the correct locking access code. 

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
        self.lock_breaker_counter = 0
    
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
            self.listOfNums.append(n)
            bruteForce.main_unlock = False
        self.listOfNums.sort()
        
        
        self.max_value = max(self.listOfNums)
        self.min_value = min(self.listOfNums)
        self.avg_value = 0 if len(self.listOfNums) == 0 else sum(self.listOfNums)/len(self.listOfNums)
        return(str(self.listOfNums)+"\n"+
                "The Minimum digits to Unlock: " + str(self.min_value)+"\n" 
              + "The Maximum digits to Unlock: " + str(self.max_value)+"\n"
              + "The Average digits to Unlock: " + str(self.avg_value))    
        
    def WaitAndCheck(self, trials = None):
        if trials == None or trials <= 1:
            trials = 5 
        
        bruteForce = SecurityEngine()
    
        for i in range(trials):
            
            while bruteForce.main_unlock != True:
                n = random.randint(0,1000000000) # This will generate a random num between 0 and 1 billion
                bruteForce.setData(str(n))
                bruteForce.currentState()
                self.lock_breaker_counter += 1
                
            bruteForce.main_unlock = False
            self.listOfNums2.append(self.lock_breaker_counter)
        
        self.listOfNums2.sort()
        self.avg_value = 0 if len(self.listOfNums2) == 0 else sum(self.listOfNums2)/len(self.listOfNums2)
        self.avg_value=(math.trunc(self.avg_value))
        return(str(self.listOfNums2)+"\n"+
               "The Average time to Unlock is " + str(self.avg_value) +" seconds")
        
   
########################################################################################################################
######################################                                      ############################################
######################################     Testing     the code             ############################################
######################################                                      ############################################
########################################################################################################################
# testRanGen = ranNumGen()
# print(testRanGen.bruteForce())
# print(testRanGen.resultsCheck())
# print(testRanGen.WaitAndCheck())
