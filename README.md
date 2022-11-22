# Security_Device
The purpose of this project is to use Finite Automata concepts in solving real-life problems.

# Author 
Created by Mitansh Chaudhari   
Software Lincense: Public Domain, Anyone can use and change it or incorporate code from this software into an application 

# what does the program do?


1. My program will simulate a security device similar to those installed in homes and offices. The program will read from a user-entered string and a random number-generated string to decide whether the user or the random number generated has entered the correct access code. There are two parts to this Security Device program.

2. The first part will read user input to unlock the lock if it finds the correct unlocking access code. Likewise, it will also lock the lock if it finds a valid locking code. This part of the program will output the current state, such as Lock and Unlock and give stats on the number of attempts, the number of times unlocked and the number of times locked. The program discards characters other than digits 0 through 9. As soon as the last digit of the access code is entered, my program will signal the action "State = UnLock" when the program is in the Lock state. Likewise, it will signal the action "State = Lock," when the user has entered a correct locking code while in the Unlock state. If the program is in the lock state and the user enters an incorrect unlocking code, it will also signal the action "State = Lock." Similarly, if the program is currently in the Unlock state and the user enters an incorrect locking code, it will signal the action "State = UnLock."
      * You can find the Python files related to the program's first part in the project's app folder.
      * The Python file labeled SecurityEngine.py performs all the tasks described above. Two more files extend from SecurityEngine.py.
      * The first is the test_security_engine.py which tests the methods in the   SecurityEngine.py and helps us generate unit test coverage for the first part of the program.
      * The second is InterfaceSecurityEngine.py which acts as the executable file allowing you to see the functionality of the SecurityEngine.py file and get the chance to unlock and lock the device. Here you get to interact with the program. 
 3. The second part of the program tests how long it takes to unlock the lock using a randomly generated sequence of numerical digits. First, the program generates a random number input string for the security device and tries to unlock the lock while ignoring the one-second wait time. The program runs at full speed, repeats as much as the user wants, and if no input given, defaults to five trails to produce the results: min, max, and average digits to unlock. Second, the program calculates the average time to break the lock if one has to wait one second to see if it is unlocked or not.
      * You can find the Python files related to the program's second part in the project's app folder. 
      * The Python file labeled RanNumGen.py performs all the tasks described above. Two more files extend from RanNumGen.py.
      * The first is the test_ranNumGen.py which tests the methods in the RanNumGen.py and helps us generate unit test coverage for the second part of the program.
      * The second is InterfaceRanNumGen.py which acts as the executable file allowing you to see the functionality of the RanNumGen.py file and get the chance to interact with the RanNumGen.py program. 
      
    
     
# How to build and run the executable?
1. After cloning my project repository(Security_Device) into your local directory on your test machine, please open the terminal.
2. To build and run the executable, you will need to have Python3 installed on your computer. To check if Python3 is installed, type: **python –version**
if not installed, please download the latest version from https://www.python.org/downloads/

# How to generate unit test coverage?

# The Platform it's been tested on: 




