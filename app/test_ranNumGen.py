import unittest
from ranNumGen import  *

class TestBruteForce(unittest.TestCase):
    
    def test_brute_force_with_no_parameters(self):
        testRanGen = ranNumGen()
        self.assertEqual(testRanGen.bruteForce(), testRanGen.listOfNums)
        
    def test_brute_force_with_parameters(self):
        testRanGen2 = ranNumGen()
        self.assertEqual(testRanGen2.bruteForce(2), testRanGen2.listOfNums)
        self.assertEqual(testRanGen2.bruteForce(0), testRanGen2.listOfNums)
        
        
class TestResultsCheck(unittest.TestCase):
    def test_results_checks_format(self):
        testRanGen3 = ranNumGen()
        testRanGen3.bruteForce()
        self.assertEqual(testRanGen3.resultsCheck(), "The Minimum tries to Unlock: " + str(testRanGen3.min_value)+"\n" 
              + "The Maximum tries to Unlock: " + str(testRanGen3.max_value)+"\n"
              + "The Average tries to Unlock " + str(testRanGen3.avg_value))
        
        
if __name__ == '__main__':
    unittest.main()
        
        
        


