import unittest
from ranNumGen import  *

class TestBruteForce(unittest.TestCase):
    
    def test_brute_force_with_no_parameters(self):
        testRanGen = ranNumGen()
        self.assertEqual(testRanGen.bruteForce(), (str(testRanGen.listOfNums)+"\n"+
                "The Minimum digits to Unlock: " + str(testRanGen.min_value)+"\n" 
              + "The Maximum digits to Unlock: " + str(testRanGen.max_value)+"\n"
              + "The Average digits to Unlock: " + str(testRanGen.avg_value)))
        
    def test_brute_force_with_parameters(self):
        testRanGen2 = ranNumGen()
        self.assertEqual(testRanGen2.bruteForce(2), (str(testRanGen2.listOfNums)+"\n"+
                "The Minimum digits to Unlock: " + str(testRanGen2.min_value)+"\n" 
              + "The Maximum digits to Unlock: " + str(testRanGen2.max_value)+"\n"
              + "The Average digits to Unlock: " + str(testRanGen2.avg_value)))
        
        self.assertEqual(testRanGen2.bruteForce(3), (str(testRanGen2.listOfNums)+"\n"+
                "The Minimum digits to Unlock: " + str(testRanGen2.min_value)+"\n" 
              + "The Maximum digits to Unlock: " + str(testRanGen2.max_value)+"\n"
              + "The Average digits to Unlock: " + str(testRanGen2.avg_value)))
        
           
class TestWaitAndCheckMethod(unittest.TestCase):
    def test_wait_one_sec_calc(self):
         testRanGen = ranNumGen()
         self.assertEqual(testRanGen.WaitAndCheck(), str(testRanGen.listOfNums2)+"\n"+
               "The Average time to Unlock is " + str(testRanGen.avg_value) +" seconds")
         # print("The Average time to Unlock is " + str(testRanGen.avg_value) +" seconds")
        
        
if __name__ == '__main__':
    unittest.main()
        
        
        


