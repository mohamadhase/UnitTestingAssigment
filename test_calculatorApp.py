from ast import Add
from asyncio.windows_events import NULL
from decimal import DivisionUndefined
import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *
import calculatorApp


class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")

    #Calculate 
    def test_CalculateTestCase1(self):
        self.assertRaises(ValueError, calculate, '1',0,0) 

    def test_CalculateTestCase2(self):
        self.assertRaises(Exception, calculate, 5,6,3) 

    def test_CalculateTestCase3(self):
        with mock.patch('calculatorApp.add', return_value = 11):
            result = calculate('1',5,6)
        self.assertEqual(result, 11)

    def test_CalculateTestCase4(self):
        with mock.patch('calculatorApp.subtract', return_value = -1):
            result = calculate('2',5,6)
        self.assertEqual(result, -1)
    def test_CalculateTestCase5(self):
        with mock.patch('calculatorApp.multiply', return_value = 30):
            result = calculate('3',5,6)
        self.assertEqual(result, (5,'*',6,'=',30))


    def test_CalculateTestCase6(self):
        with mock.patch('calculatorApp.divide', return_value = 2):
            result = calculate('4',12,6)
        self.assertEqual(result, (12,'/',6,'=',2))


    def test_CalculateTestCase7(self):
        self.assertRaises(ZeroDivisionError, calculate, 4,12,0) 


    #add 
    def test_AddTestCase1(self):
        self.assertEqual(add(1,1), 2)
  

    #CheckUserInput 
    def test_CheckUserInputTestCase1(self):
        self.assertRaises(ValueError, check_user_input,"")    

    def test_CheckUserInputTestCase2(self):
        self.assertEqual(check_user_input("5"), 5)

    def test_CheckUserInputTestCase3(self):
        self.assertEqual(check_user_input("5.5"), 5.5)

    def test_CheckUserInputTestCase4(self):
        self.assertRaises(ValueError, check_user_input,"w")    


    #divide 
    def test_DivideTestCase1(self):
        self.assertRaises(ZeroDivisionError, divide,12,0)    

    def test_DivideTestCase2(self):
        self.assertEqual(divide(0,6), 0)

    def test_DivideTestCase3(self):
        self.assertEqual(divide(12,6), 2)

    #isExit 
    def test_isExitTestCase1(self):
        self.assertEqual(isExit("no"), True)

    def test_isExitTestCase2(self):
        self.assertEqual(isExit("yes"), False)

    def test_isExitTestCase3(self):
        self.assertRaises(ValueError, isExit,'w')    


    def tearDown(self):
        print("tearDown .. ")


    #multiply 
    def test_multiplyTestCase1(self):

        self.assertEqual(multiply(10,10), 100)

    
    #subtract 
    def test_subtractTestCase1(self):
        self.assertEqual(subtract(10,10), 0)
if __name__ == '__main__':
	unittest.main()
