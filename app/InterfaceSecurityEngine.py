from SecurityEngine import *
from ranNumGen import *


print("###############################################################################################################################\n"+
"###############################################################################################################################\n"+
"######################################                                              ###########################################\n"+
"######################################  Welcome to the Security Device Interface!!  ###########################################\n"+
"######################################                                              ###########################################\n"+
"######################################  Here you will see the functionality         ###########################################\n"+
"######################################  of the Security Device and will get the     ###########################################\n"+
"######################################  chance to unlock and lock the Device.       ###########################################\n"+
"######################################                                              ###########################################\n"+
"###############################################################################################################################\n"+
"###############################################################################################################################")
print(" ")
print("Here State represents if the lock is currently Unlocked or Locked.\nThe program also gives stats on number attempts and the times you Locked and Unlocked the system.")
print(" ")
print("Lets try to Unlock the device with the our Unlock Code: 204801")
testEngine = SecurityEngine()
testEngine.setData("204801")
testEngine.currentState()
print(testEngine.statsOfState())
print(" ")
print("Lets try to Lock the device with the our Lock Code: 204804")
testEngine.setData("204804")
testEngine.currentState()
print(testEngine.statsOfState())
print(" ")
print("Will the Engine quietly discard any character other than number 0-9?\nLets try it with the string: cs330Mitanshchaudhari")
testEngine2 = SecurityEngine()
testEngine2.setData("cs330Mitanshchaudhari")
testEngine2.currentState()
print(testEngine2.statsOfState())
print(" ")
print("Lets try alphabets with our Unlock code: cs330Mitanshchaudhari204801 ")
testEngine3 = SecurityEngine()
testEngine3.setData("cs330Mitanshchaudhari204801")
testEngine3.currentState()
print(testEngine3.statsOfState())
print(" ")
print("Will the Device unlock as soon as the engine finds the last correct letter of the access code?\nLets try it with the string: 91352020480145")
testEngine4 = SecurityEngine()
testEngine4.setData("91352020480145")
testEngine4.currentState()
print(testEngine4.statsOfState())
print(" ")
print("Will the Device Lock as soon as the engine finds the last correct letter of the locking code?\nLets try it with the string: 91352020480445")
testEngine4.setData("91352020480445")
testEngine4.currentState()
print(testEngine4.statsOfState())
print(" ")
print("Lets try a long string containing both the access code and the lock code to \nsee if each state is triggered. String contains the access code two times \nand the lock code once: 6347987620480131420488204804366117780865122048011390389148" )
testEngine5 = SecurityEngine()
testEngine5.setData("6347987620480131420488204804366117780865122048011390389148")
testEngine5.currentState()
print(testEngine5.statsOfState())
print(" ")
print("This Concludes our testing with set data points. Now its your turn to Unlock and \nLock the Device(p.s please pretend you don't know the codes). Good Luck!!!")
testEngine6 = SecurityEngine()
testEngine6.setData()
testEngine6.currentState()
print(testEngine6.statsOfState())
print(" ")












