from SecurityEngine import *
from ranNumGen import *
print(" ")
print("###############################################################################################################################\n"+
"###############################################################################################################################\n"+
"###################################    Lets try to break the lock with random sequence of numbers!!    ########################\n"+
"###############################################################################################################################\n"+
"###############################################################################################################################")
print(" ")
print("The program will generate random sequence of numerical digits as the input.\nThe program will then generate min, max, and average based on desired trails by the user")
print(" ")
print("Repeating the test more than 5 trails will take more than 35sec, therefore test accordingly")
print(" ")
trails = input("How many trials would you like for estimating the digits to unlock?\nTrials = ")
print("")
trails2 = input("How many trials would you like for estimating the average time to unlock?\nTrials =  ")
print(" ")
print(" ")
testRanGen = ranNumGen()
testRanGen.bruteForce(int(trails))

testRanGen2 = ranNumGen()
testRanGen2.WaitAndCheck(int(trails2))
print(" ")
print(" ")
print("When we brute force the system with " + str(trails)+ " trials, Following are the results:\n"+ str(testRanGen.listOfNums)+"\n"+
                "The Minimum digits to Unlock: " + str(testRanGen.min_value)+"\n" 
              + "The Maximum digits to Unlock: " + str(testRanGen.max_value)+"\n"
              + "The Average digits to Unlock: " + str(testRanGen.avg_value))
print(" ")
print(" ")
print("The average time to unlock while waiting 1 sec with "+ str(trails2)+ " trials:\n" + str(testRanGen2.listOfNums2)+"\n"+
               "The Average time to Unlock is " + str(testRanGen2.avg_value) +" seconds")