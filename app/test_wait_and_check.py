import unittest
from ranNumGen import  *
from SecurityEngine import *

class TestWaitAndCheckMethod(unittest.TestCase):
    def test_wait_one_sec_calc(self):
         testRanGen = ranNumGen()
         testRanGen.WaitAndCheck()
         self.assertEqual(testRanGen.WaitAndCheck(), "The Average tries to Unlock " + str(testRanGen.avg_value) +" seconds") 
         
         
        
if __name__ == '__main__':
    unittest.main()
        
