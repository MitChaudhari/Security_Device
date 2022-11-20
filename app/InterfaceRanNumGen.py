from SecurityEngine import *
from ranNumGen import *
testRanGen = ranNumGen()
testRanGen.bruteForce(2)

testRanGen2 = ranNumGen()
testRanGen2.bruteForce()
print(" ")
print(" ")
print("###############################################################################################################################\n"+
"###############################################################################################################################\n"+
"###################################    Lets try to break the lock with random sequence of numbers!!    ########################\n"+
"###############################################################################################################################\n"+
"###############################################################################################################################")
print(" ")
print("The program will generate random sequence of numerical digits as the input.\nThe program will then generate min, max, and average based on desired trails by the user")
print(" ")
print("Lets brute force the system with 2 trials\n"+ str(testRanGen.listOfNums)+"\n"+str(testRanGen.resultsCheck()))
print(" ")
print("Lets brute force the system with 5 trials\nDefault trails is set to five therefore no parameter needed.\n"+ str(testRanGen2.listOfNums)+"\n"+str(testRanGen2.resultsCheck()))