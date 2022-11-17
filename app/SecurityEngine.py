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
        self.data = "1"
        self.unlock_state_counter = 0
        self.lock_state_counter = 0
        self.unknown_state_counter = 0
        self.total_state = 0
        self.methodscheck = ""
                     
    
    def setData(self, userData = ""):
        self.methodscheck = userData
        if userData != "":
            self.data = userData
        else:
            self.data = input("Enter a Number: ")
            


            
        
        # self.data = inputData

    def currentState(self):
    
        while self.data not in ("S", "s"):
            self.Lock = False              # This informs of what state is lock in 
            self.UnLock = False
            
            for i in range(len(self.data)):
                if self.data[i:i+6] == self.unlock_code:
                    self.UnLock = True 
                    self.Lock = False 
                    self.unlock_state_counter += 1
                if self.data[i:i+6] == self.lock_code:
                    self.Lock = True 
                    self.UnLock = False 
                    self.lock_state_counter+=1 
                    
            if self.UnLock:
                print("State = UnLock")
                if self.methodscheck != "":
                    self.data = "S"
                else:
                    self.data = input("To stop the Engine Press s or Now try to Lock the Engine: ")
                
            elif self.Lock:
                print("State = Lock")
                if self.methodscheck != "":
                    self.data = "S"
                else:
                    self.data = input("To stop the Engine Press s or Try to UnLock the Engine: ")
                
                # self.data = input("State = Lock\n" + "To stop the Engine Press s or Try to UnLock the Engine: ")
            else:
                print("State = Unknown")
                if self.methodscheck != "":
                    self.data = "S"
                else:
                    self.data = input("To stop the Engine Press s or Try to UnLock or Lock the Engine: ")
    
                self.unknown_state_counter += 1
            
                
    def statsOfState(self): 
        
        self.total_state = self.unlock_state_counter+self.lock_state_counter+self.unknown_state_counter
        print("Out of " +str(self.total_state)+ " trys, you unlocked " + 
                        str(self.unlock_state_counter)+ " times and Locked " +
                        str(self.lock_state_counter)+ " times")
        
        
            
            
########################################################################################################################
######################################                                      ############################################
######################################     Testing     the code             ############################################
######################################                                      ############################################
########################################################################################################################
    
        #6347987620480131420488204804366117780865122048011390389148
                
                    


print("Testing:\n")

testEngine = SecurityEngine()
testEngine.setData("204801")
testEngine.currentState()
testEngine.statsOfState()
print(" ")
testEngine1 = SecurityEngine()
testEngine1.setData("204804")
testEngine1.currentState()
testEngine1.statsOfState()
print(" ")
testEngine1 = SecurityEngine()
testEngine1.setData("6347987642332131420488423324366117780865124233211390389148")
testEngine1.currentState()
testEngine1.statsOfState()
print(" ")
testEngine1 = SecurityEngine()
testEngine1.setData("6347987620480131420488204804366117780865122048011390389148")
testEngine1.currentState()
testEngine1.statsOfState()
print(" ")
testEngine1 = SecurityEngine()
testEngine1.setData()
testEngine1.currentState()
testEngine1.statsOfState()






    
        
     
            
            
    
        
        
        
        
        
        

        
    
    
 




