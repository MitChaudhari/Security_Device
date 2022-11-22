# Security_Device
The purpose of this project is to use Finite Automata concepts in solving real-life problems.

# Author 
Created by Mitansh Chaudhari :  
Software Lincense: Public Domain, Anyone can use and change it or incorporate code from this software into an application 

# what does the program do?


1. My program will simulate a security device similar to those installed in homes and offices. The program will read from a user-entered string and a random number-generated string to decide whether the user or the random number generated has entered the correct access code. There are two parts to this Security Device program.
<br/>
2. The first part will read user input to unlock the lock if it finds the correct unlocking access code. Likewise, it will also lock the lock if it finds a valid locking code. This part of the program will output the current state, such as Lock and Unlock and give stats on the number of attempts, the number of times unlocked and the number of times locked. The program discards characters other than digits 0 through 9. As soon as the last digit of the access code is entered, my program will signal the action "State = UnLock" when the program is in the Lock state. Likewise, it will signal the action "State = Lock," when the user has entered a correct locking code while in the Unlock state. If the program is in the lock state and the user enters an incorrect unlocking code, it will also signal the action "State = Lock." Similarly, if the program is currently in the Unlock state and the user enters an incorrect locking code, it will signal the action "State = UnLock."
      * You can find the Python files related to the program's first part in the project's app folder.
      
    

# How to build and run the executable?

# How to generate unit test coverage?

# The Platform it's been tested on: 




