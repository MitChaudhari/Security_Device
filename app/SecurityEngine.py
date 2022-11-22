# CS330 A security Device Assignment Version 1, 11/15/2022
# Created By: Mitansh Chaudahri 
from pickle import FALSE, TRUE
import random

# This class will implement Security Engine 
# that will unlock the lock when it finds the 
# # correct un-locking access and lock  when it finds 
# the correct locking access code. 

class SecurityEngine: 
    
    def __init__(self):
        self.unlock_code = "204801"    #This is the unlcok code 
        self.lock_code = "204804"      # This is the lock code            
        self.Lock = False              # This informs of what state is lock in 
        self.UnLock = False            # This informs of what state is unlock in
        self.data = "1"
        self.unlock_state_counter = 0
        self.lock_state_counter = 0
        self.unknown_state_counter = 0
        self.total_state = 0
        self.methodscheck = ""
        self.main_lock = False
        self.main_unlock = False
        
    def state_checker(self):
        if self.UnLock:
            return("State = UnLock")
        else: 
            return("State = Lock")
                     
    
    def setData(self, userData = ""):
        self.methodscheck = userData
        if userData != "":
            self.data = userData
        else:
            self.data = input("Enter the Passcode: ")

    def currentState(self):
    
        while self.data not in ("S", "s"):
            self.Lock = False             # resetting the check Condition  
            self.UnLock = False
            
            for i in range(len(self.data)):
                if self.data[i:i+6] == self.unlock_code:
                    self.UnLock = True 
                    print(("State = UnLock"))
                    self.Lock = False 
                    self.main_unlock = True
                    self.main_lock = False
                    self.unlock_state_counter += 1
                    
                    
                if self.data[i:i+6] == self.lock_code:
                    self.lock_state_counter+=1
                    self.Lock = True 
                    print(("State = Lock"))
                    self.UnLock = False 
                    self.main_unlock = False
                    self.main_lock = True
                    
                    
            if self.UnLock:
                if self.methodscheck != "":
                    self.data = "S"
                else:
                    self.data = input("To stop the Engine, Press S or Try to Lock the Lock: ")
    
            elif self.Lock:
                if self.methodscheck != "":
                    self.data = "S"
                else:
                    self.data = input("To stop the Engine, Press S or Try to UnLock the Lock: ")
                   
            else:                
                if self.main_unlock:
                    print("State = UnLock")
                    
                else:
                    print("State = Lock")
                if self.methodscheck != "":
                    self.data = "S"
                else:
                    if self.main_unlock:
                        self.data = input("To stop the Engine Press s or Try to Lock the Lock: ")
                    else:
                        self.data = input("To stop the Engine Press s or Try to UnLock the Lock: ")
                self.unknown_state_counter += 1
                        
        return SecurityEngine.state_checker(self)
                         
    def statsOfState(self): 
        
        self.total_state = self.unlock_state_counter + self.lock_state_counter + self.unknown_state_counter
        return(("Out of " +str(self.total_state)+ " trys, you unlocked " + 
                        str(self.unlock_state_counter)+ " times and Locked " +
                        str(self.lock_state_counter)+ " times"))
        
        
        

