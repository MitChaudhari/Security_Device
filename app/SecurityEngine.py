# CS330 A security Device Assignment Version 1, 11/15/2022
# Created By: Mitansh Chaudahri 
from pickle import FALSE

# This class will implement Security Engine 
# that will unlock the lock when it finds the 
# # correct un-locking access and lock  when it finds 
# the correct locking access code. 

class SecurityEngine: 
    
    def __init__(self):
        self.unlock_code = "204801"    #This is the unlcok code 
        self.lock_code = "204804"      # This is the lock code            
        # self.current_state = ""        # This tells the state if it's lock or unlock
        self.Lock = False              # This informs of what state is lock in 
        self.UnLock = False            # This informs of what state is unlock in
        self.data = ""                 # This is user data which will check 
        
    def isLock(self) -> bool: 
        return self.Lock
    
    def isUnLock(self) -> bool:
        return self.UnLock
    
    def currentState(self) -> str:
        
        if SecurityEngine.isUnLock(self) == True:
            return "Unlock"
        else:
            return "Lock" 
        
    def getData(self):
        input_string = input("Enter a string: ")
        i = 0
        output_string = "" 
        for character in input_string:
            if character.isdigit():
                output_string += character
        return output_string
    
    
        
     
            
            
    
        
        
        
        
        
        

        
    
    
 




