import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_01postfix_eval_add(self):
        self.assertAlmostEqual(12.0, postfix_eval("12"))
        self.assertAlmostEqual(12.0, postfix_eval("12.0"))
        self.assertAlmostEqual(12.0, postfix_eval("5 7 +"))
        self.assertAlmostEqual(12.1, postfix_eval("5.1 7 +"))
        self.assertAlmostEqual(12.1, postfix_eval("5 7.1 +"))
        self.assertAlmostEqual(12.2, postfix_eval("5.1 7.1 +"))      
        self.assertAlmostEqual(-2.1, postfix_eval("5.1 -7.2 +"))
        self.assertAlmostEqual(2.1,  postfix_eval("-5.1 7.2 +"))
        self.assertAlmostEqual(-12.3, postfix_eval("-5.1 -7.2 +"))
        self.assertAlmostEqual(23.1, postfix_eval("5 7.1 + 11 +"))
        self.assertAlmostEqual(23.1, postfix_eval("5 7.1 11 + +"))      
        self.assertAlmostEqual(20.1, postfix_eval("5 7.1 + 11 + -3 +"))
        self.assertAlmostEqual(20.1, postfix_eval("5 7.1 11 -3 + + +"))      
        self.assertAlmostEqual(4.1, postfix_eval("5 7.1 + -11 + 3 +"))
        self.assertAlmostEqual(4.1, postfix_eval("5 7.1 -11 3 + + +"))      
        self.assertAlmostEqual(11.9, postfix_eval("5 -7.1 + 11 + 3 +"))
        self.assertAlmostEqual(11.9, postfix_eval("5 -7.1 11 3 + + +"))    
        self.assertAlmostEqual(16.1, postfix_eval("-5 7.1 + 11 + 3 +"))
        self.assertAlmostEqual(16.1, postfix_eval("-5 7.1 11 3 + + +"))

    def test_02_postfix_eval_sub(self):
        self.assertAlmostEqual(-2.0, postfix_eval("5 7 -"))
        self.assertAlmostEqual(-1.9, postfix_eval("5.1 7 -"))
        self.assertAlmostEqual(-2.1, postfix_eval("5 7.1 -"))
        self.assertAlmostEqual(-2.0, postfix_eval("5.1 7.1 -"))     
        self.assertAlmostEqual(12.3, postfix_eval("5.1 -7.2 -"))
        self.assertAlmostEqual(-12.3, postfix_eval("-5.1 7.2 -"))
        self.assertAlmostEqual(2.1, postfix_eval("-5.1 -7.2 -"))
        self.assertAlmostEqual(-13.1, postfix_eval("5 7.1 - 11 -"))
        self.assertAlmostEqual(8.9, postfix_eval("5 7.1 11 - -"))      
        self.assertAlmostEqual(-10.1, postfix_eval("5 7.1 - 11 - -3 -"))
        self.assertAlmostEqual(11.9, postfix_eval("5 7.1 11 -3 - - -"))      
        self.assertAlmostEqual(5.9, postfix_eval("5 7.1 - -11 - 3 -"))
        self.assertAlmostEqual(-16.1, postfix_eval("5 7.1 -11 3 - - -"))      
        self.assertAlmostEqual(-1.9, postfix_eval("5 -7.1 - 11 - 3 -"))
        self.assertAlmostEqual(20.1, postfix_eval("5 -7.1 11 3 - - -"))      
        self.assertAlmostEqual(-26.1, postfix_eval("-5 7.1 - 11 - 3 -"))
        self.assertAlmostEqual(-4.1, postfix_eval("-5 7.1 11 3 - - -"))

    def test_03_postfix_eval_mult(self):
        self.assertAlmostEqual(35.0, postfix_eval("5 7 *"))
        self.assertAlmostEqual(35.7, postfix_eval("5.1 7 *"))
        self.assertAlmostEqual(35.5, postfix_eval("5 7.1 *"))
        self.assertAlmostEqual(36.21, postfix_eval("5.1 7.1 *"))
        self.assertAlmostEqual(-36.72, postfix_eval("5.1 -7.2 *"))
        self.assertAlmostEqual(-36.72, postfix_eval("-5.1 7.2 *"))
        self.assertAlmostEqual(36.72, postfix_eval("-5.1 -7.2 *"))
        self.assertAlmostEqual(390.5, postfix_eval("5 7.1 * 11 *"))
        self.assertAlmostEqual(390.5, postfix_eval("5 7.1 11 * *"))      
        self.assertAlmostEqual(-1171.5, postfix_eval("5 7.1 * 11 * -3 *"))
        self.assertAlmostEqual(-1171.5, postfix_eval("5 7.1 11 -3 * * *"))      
        self.assertAlmostEqual(-1171.5, postfix_eval("5 7.1 * -11 * 3 *"))
        self.assertAlmostEqual(-1171.5, postfix_eval("5 7.1 -11 3 * * *"))      
        self.assertAlmostEqual(-1171.5, postfix_eval("5 -7.1 * 11 * 3 *"))
        self.assertAlmostEqual(-1171.5, postfix_eval("5 -7.1 11 3 * * *"))      
        self.assertAlmostEqual(-1171.5, postfix_eval("-5 7.1 * 11 * 3 *"))
        self.assertAlmostEqual(-1171.5, postfix_eval("-5 7.1 11 3 * * *"))

    def test_04_postfix_eval_basic_div(self):
        self.assertAlmostEqual(0.714285714, postfix_eval("5 7 /"))
        self.assertAlmostEqual(0.728571429, postfix_eval("5.1 7 /"))
        self.assertAlmostEqual(0.704225352, postfix_eval("5 7.1 /"))
        self.assertAlmostEqual(0.718309859, postfix_eval("5.1 7.1 /"))      
        self.assertAlmostEqual(-0.708333333, postfix_eval("5.1 -7.2 /"))
        self.assertAlmostEqual(-0.708333333, postfix_eval("-5.1 7.2 /"))
        self.assertAlmostEqual(0.708333333, postfix_eval("-5.1 -7.2 /"))
        self.assertAlmostEqual(0.064020487, postfix_eval("5 7.1 / 11 /"))
        self.assertAlmostEqual(7.746478873, postfix_eval("5 7.1 11 / /"))      
        self.assertAlmostEqual(-0.021340162, postfix_eval("5 7.1 / 11 / -3 /"))
        self.assertAlmostEqual(-2.582159624, postfix_eval("5 7.1 11 -3 / / /"))      
        self.assertAlmostEqual(-0.021340162, postfix_eval("5 7.1 / -11 / 3 /"))
        self.assertAlmostEqual(-2.582159624, postfix_eval("5 7.1 -11 3 / / /"))      
        self.assertAlmostEqual(-0.021340162, postfix_eval("5 -7.1 / 11 / 3 /"))
        self.assertAlmostEqual(-2.582159624, postfix_eval("5 -7.1 11 3 / / /"))     
        self.assertAlmostEqual(-0.021340162, postfix_eval("-5 7.1 / 11 / 3 /"))
        self.assertAlmostEqual(-2.582159624, postfix_eval("-5 7.1 11 3 / / /"))

    def test_05_postfix_eval_mixed(self):
        self.assertAlmostEqual(25, postfix_eval("25"))
        self.assertAlmostEqual(1.234, postfix_eval("1.234"))
        self.assertAlmostEqual(-5, postfix_eval("-5"))
        self.assertAlmostEqual(-0.09523809, postfix_eval("2 3 4 5 6 + - * /"))
        self.assertAlmostEqual(0.83333333, postfix_eval("2 3 + 4 - 5 * 6 /"))
        self.assertAlmostEqual(1.25, postfix_eval("2 3 4 5 6 - * / +"))
        self.assertAlmostEqual(5.2, postfix_eval("2 3 - 4 * 5 / 6 +"))
        self.assertAlmostEqual(-1.13333333, postfix_eval("2 3 4 5 6 * / + -"))
        self.assertAlmostEqual(0.5, postfix_eval("2 3 * 4 / 5 + 6 -"))
        self.assertAlmostEqual(-3.66666666, postfix_eval("2 3 4 5 6 / + - *"))
        self.assertAlmostEqual(-2.0, postfix_eval("2 3 / 4 + 5 - 6 *"))
        self.assertAlmostEqual(1.66666666, postfix_eval("2 3 4 5 6 / * - +"))
        self.assertAlmostEqual(3.66666666, postfix_eval("2 3 / 4 * 5 - 6 +"))
        self.assertAlmostEqual(-0.0869565217, postfix_eval("2 3 4 5 6 * - + /"))
        self.assertAlmostEqual(1.16666666, postfix_eval("2 3 * 4 - 5 + 6 /"))
        self.assertAlmostEqual(2.0, postfix_eval("2 3 4 5 6 - + / *"))
        self.assertAlmostEqual(3.6, postfix_eval("2 3 - 4 + 5 / 6 *"))
        self.assertAlmostEqual(0.90909090, postfix_eval("2 3 4 5 6 + / * -"))
        self.assertAlmostEqual(0.25, postfix_eval("2 3 + 4 / 5 * 6 -"))
        self.assertAlmostEqual(5.0, postfix_eval("6 4 3 + 2 - * 6 /"))
        self.assertAlmostEqual(18.0, postfix_eval("5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +"))

    def test_06_postfix_eval_complex(self):
        #to ensure that everything in O(1)
        for i in range(5000):
            self.assertAlmostEqual(5589.854285714286, postfix_eval("3 2 + 8 3 / 17 * + 12 4.2 / 1.2 / 8 6 * - 6.9 17 * 23 6 / + 2.2 - 3.2 - 56 21 / 1.4 * - 2.3 4.1 * + * -"))
            self.assertAlmostEqual(32.72934207499424, postfix_eval("38 1.2 * 3.6 2.8 / + 6 - 3.7 2 / 5 / + 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - +"))
            self.assertAlmostEqual(34.72934207499424, postfix_eval("2 38 1.2 * 3.6 2.8 / + 6 - 3.7 2 / 5 / + 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - + 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - +"))
            self.assertAlmostEqual(30.72934207499424, postfix_eval("38 1.2 * 3.6 2.8 / + 6 - 3.7 2 / 5 / + 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +"))
            self.assertAlmostEqual(83442.42761745711, postfix_eval("38 1.2 * 3.6 2.8 / + 6 - 3.7 ** 2 / 5 / 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +"))
            self.assertAlmostEqual(2.819617757458424, postfix_eval("38 1.2 3.6 ** ** 2.8 / 6 - 3.7 / 2 / 5 / 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +"))
            self.assertAlmostEqual(-1259.3992086513265, postfix_eval("38 1.2 3.6 ** ** 2.8 / 6 3.7 ** 2 / 5 * - 3 - 23 + 1.1 / 2.2 + -2.4 5 1 ** ** - 1.6 3 / 9 2.8 -3 ** ** / 6.2 4 12.8 ** / 2 * 1.1 / 4.4 3.2 1.1 ** / 5.2 / 9.9 * - - + -2 +"))
            self.assertAlmostEqual(88243.62458440628, postfix_eval("2 38 1.2 * 3.6 1.8 .25 1.7 ** ** * 2 / 5 3 ** / + 23 1.1 2.2 ** / + 2.4 5 / - 1 - + 1.6 3 9 ** * 2.8 * 3 6.2 4 12.8 2 1.1 ** * 4.4 3.2 / - 1.1 5.2 7.7 ** / - ** / ** - +"))

    def test_07_postfix_eval_test_postfix_exceptions(self):
        try:
            postfix_eval("99 38 1.2 * 3.6 2.8 / + 6 - 3.7 2 / 5 / + 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")        
        try:
            postfix_eval("38 1.2 * 3.6 2.8 / + 6 - 3.7 ** 2 / 5 / 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 blah / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")        
        try:
            postfix_eval("1.2 * 3.6 2.8 / + 6 - 3.7 2 / 5 / + 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")     
        try:
            postfix_eval("12 1.2 * 10 10 - / 6 - 3.7 ** 2 / 5 / 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 10 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +")
            self.fail()
        except ValueError as e:
            pass        
                

    def test_16_prefix_to_postfix_basic(self):
        self.assertEqual(prefix_to_postfix("+ + + 5 -7.1 11 3"), "5 -7.1 + 11 + 3 +")
        self.assertEqual(prefix_to_postfix("+ 5 + -7.1 + 11 3"), "5 -7.1 11 3 + + +")
        self.assertEqual(prefix_to_postfix("+ + + -5 7.1 11 3"), "-5 7.1 + 11 + 3 +")
        self.assertEqual(prefix_to_postfix("+ -5 + 7.1 + 11 3"), "-5 7.1 11 3 + + +")
        self.assertEqual(prefix_to_postfix("- - - 5 -7.1 11 3"), "5 -7.1 - 11 - 3 -")
        self.assertEqual(prefix_to_postfix("- 5 - -7.1 - 11 3"), "5 -7.1 11 3 - - -")
        self.assertEqual(prefix_to_postfix("- - - -5 7.1 11 3"), "-5 7.1 - 11 - 3 -")
        self.assertEqual(prefix_to_postfix("- -5 - 7.1 - 11 3"), "-5 7.1 11 3 - - -")
        self.assertEqual(prefix_to_postfix("* * * 5 -7.1 11 3"), "5 -7.1 * 11 * 3 *")
        self.assertEqual(prefix_to_postfix("* 5 * -7.1 * 11 3"), "5 -7.1 11 3 * * *")
        self.assertEqual(prefix_to_postfix("* * * -5 7.1 11 3"), "-5 7.1 * 11 * 3 *")
        self.assertEqual(prefix_to_postfix("* -5 * 7.1 * 11 3"), "-5 7.1 11 3 * * *")
        self.assertEqual(prefix_to_postfix("/ / / 5 -7.1 11 3"), "5 -7.1 / 11 / 3 /")
        self.assertEqual(prefix_to_postfix("/ 5 / -7.1 / 11 3"), "5 -7.1 11 3 / / /")
        self.assertEqual(prefix_to_postfix("/ / / -5 7.1 11 3"), "-5 7.1 / 11 / 3 /")
        self.assertEqual(prefix_to_postfix("/ -5 / 7.1 / 11 3"), "-5 7.1 11 3 / / /")
        self.assertEqual(prefix_to_postfix("** 2 ** 3 ** 4.4 5"), "2 3 4.4 5 ** ** **")
        self.assertEqual(prefix_to_postfix("** ** ** 2 3 4 5"), "2 3 ** 4 ** 5 **")
        self.assertEqual(prefix_to_postfix("** 2 ** 3 ** 4 5.5"), "2 3 4 5.5 ** ** **")
        self.assertEqual(prefix_to_postfix("** 2 ** ** 3.3 4 5"), "2 3.3 4 ** 5 ** **")
        self.assertEqual(prefix_to_postfix("** ** 2.2 ** 3 4 5"), "2.2 3 4 ** ** 5 **")
        
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("/ 2 * 3 - 4 + 5 6"), "2 3 4 5 6 + - * /")
        self.assertEqual(prefix_to_postfix("/ * - + 2 3 4 5 6"), "2 3 + 4 - 5 * 6 /")
        self.assertEqual(prefix_to_postfix("+ 2 / 3 * 4 - 5 6"), "2 3 4 5 6 - * / +")
        self.assertEqual(prefix_to_postfix("+ / * - 2 3 4 5 6"), "2 3 - 4 * 5 / 6 +")
        self.assertEqual(prefix_to_postfix("- 2 + 3 / 4 * 5 6"), "2 3 4 5 6 * / + -")
        self.assertEqual(prefix_to_postfix("- + / * 2 3 4 5 6"), "2 3 * 4 / 5 + 6 -")
        self.assertEqual(prefix_to_postfix("* 2 - 3 + 4 / 5 6"), "2 3 4 5 6 / + - *")
        self.assertEqual(prefix_to_postfix("* - + / 2 3 4 5 6"), "2 3 / 4 + 5 - 6 *")
        self.assertEqual(prefix_to_postfix("+ 2 - 3 * 4 / 5 6"), "2 3 4 5 6 / * - +")
        self.assertEqual(prefix_to_postfix("+ - * / 2 3 4 5 6"), "2 3 / 4 * 5 - 6 +")
        self.assertEqual(prefix_to_postfix("/ 2 + 3 - 4 * 5 6"), "2 3 4 5 6 * - + /")
        self.assertEqual(prefix_to_postfix("/ + - * 2 3 4 5 6"), "2 3 * 4 - 5 + 6 /")
        self.assertEqual(prefix_to_postfix("* 2 / 3 + 4 - 5 6"), "2 3 4 5 6 - + / *")
        self.assertEqual(prefix_to_postfix("* / + - 2 3 4 5 6"), "2 3 - 4 + 5 / 6 *")
        self.assertEqual(prefix_to_postfix("- 2 * 3 / 4 + 5 6"), "2 3 4 5 6 + / * -")
        self.assertEqual(prefix_to_postfix("- * / + 2 3 4 5 6"), "2 3 + 4 / 5 * 6 -")
        self.assertEqual(prefix_to_postfix("/ * 6 - + 4 3 2 6"), "6 4 3 + 2 - * 6 /")
        self.assertEqual(prefix_to_postfix("+ + 5 * 2 4 - + - 7 2 * 4 - / 6 2 2 4"), "5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +")

    def test_17_prefix_to_postfix_complex(self):
        self.assertEqual(prefix_to_postfix("- + + 3 2 * / 8 3 17 * - / / 12 4.2 1.2 * 8 6 + - - - + * 6.9 17 / 23 6 2.2 3.2 * / 56 21 1.4 * 2.3 4.1"), "3 2 + 8 3 / 17 * + 12 4.2 / 1.2 / 8 6 * - 6.9 17 * 23 6 / + 2.2 - 3.2 - 56 21 / 1.4 * - 2.3 4.1 * + * -")
        self.assertEqual(prefix_to_postfix("+ - - + / + - + - + * 38 1.2 / 3.6 2.8 6 / / 3.7 2 5 3 23 1.1 2.2 / 2.4 5 1 - - * / / 1.6 3 9 2.8 3 + / 6.2 4 - / * 12.8 2 1.1 / 4.4 - 3.2 * / 1.1 5.2 9.9"), "38 1.2 * 3.6 2.8 / + 6 - 3.7 2 / 5 / + 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - +")
        self.assertEqual(prefix_to_postfix("+ + 2 - - + / + - + - + * 38 1.2 / 3.6 2.8 6 / / 3.7 2 5 3 23 1.1 2.2 / 2.4 5 1 - - * / / 1.6 3 9 2.8 3 + / 6.2 4 - / * 12.8 2 1.1 / 4.4 - 3.2 * / 1.1 5.2 9.9"), "2 38 1.2 * 3.6 2.8 / + 6 - 3.7 2 / 5 / + 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - + 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - +")
        self.assertEqual(prefix_to_postfix("+ + - - + / + - + - + * 38 1.2 / 3.6 2.8 6 / / 3.7 2 5 3 23 1.1 2.2 / 2.4 5 1 - - * / / 1.6 3 9 2.8 3 + / 6.2 4 - / * 12.8 2 1.1 / 4.4 - 3.2 * / 1.1 5.2 9.9 -2"), "38 1.2 * 3.6 2.8 / + 6 - 3.7 2 / 5 / + 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +")
        self.assertEqual(prefix_to_postfix("+ + - - + / + - / / ** - + * 38 1.2 / 3.6 2.8 6 3.7 2 5 3 23 1.1 2.2 / 2.4 5 1 - - * / / 1.6 3 9 2.8 3 + / 6.2 4 - / * 12.8 2 1.1 / 4.4 - 3.2 * / 1.1 5.2 9.9 -2"), "38 1.2 * 3.6 2.8 / + 6 - 3.7 ** 2 / 5 / 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +")
        self.assertEqual(prefix_to_postfix("+ + - - + / + - / / / - / ** 38 ** 1.2 3.6 2.8 6 3.7 2 5 3 23 1.1 2.2 / 2.4 5 1 - - * / / 1.6 3 9 2.8 3 + / 6.2 4 - / * 12.8 2 1.1 / 4.4 - 3.2 * / 1.1 5.2 9.9 -2"), "38 1.2 3.6 ** ** 2.8 / 6 - 3.7 / 2 / 5 / 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +")
        self.assertEqual(prefix_to_postfix("+ + - + / + - - / ** 38 ** 1.2 3.6 2.8 * / ** 6 3.7 2 5 3 23 1.1 2.2 ** -2.4 ** 5 1 - / / 1.6 3 ** 9 ** 2.8 -3 - / * / 6.2 ** 4 12.8 2 1.1 * / / 4.4 ** 3.2 1.1 5.2 9.9 -2"), "38 1.2 3.6 ** ** 2.8 / 6 3.7 ** 2 / 5 * - 3 - 23 + 1.1 / 2.2 + -2.4 5 1 ** ** - 1.6 3 / 9 2.8 -3 ** ** / 6.2 4 12.8 ** / 2 * 1.1 / 4.4 3.2 1.1 ** / 5.2 / 9.9 * - - + -2 +")
        self.assertEqual(prefix_to_postfix("+ + 2 - - + + * 38 1.2 / / * 3.6 ** 1.8 ** .25 1.7 2 ** 5 3 / 23 ** 1.1 2.2 / 2.4 5 1 - * * 1.6 ** 3 9 2.8 ** 3 / 6.2 ** 4 - - * 12.8 ** 2 1.1 / 4.4 3.2 / 1.1 ** 5.2 7.7"), "2 38 1.2 * 3.6 1.8 .25 1.7 ** ** * 2 / 5 3 ** / + 23 1.1 2.2 ** / + 2.4 5 / - 1 - + 1.6 3 9 ** * 2.8 * 3 6.2 4 12.8 2 1.1 ** * 4.4 3.2 / - 1.1 5.2 7.7 ** / - ** / ** - +")
        self.assertEqual(prefix_to_postfix("+ 3 / * 4 2 ** - 1 5 ** 2 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(prefix_to_postfix("+ 3 * 4 ** / 2 ** - 1 5 2 3"), "3 4 2 1 5 - 2 ** / 3 ** * +")

    def test_18_prefix_to_postfix_single_value(self):
        self.assertEqual("25", prefix_to_postfix("25"))
        self.assertEqual("1.234", prefix_to_postfix("1.234"))
        self.assertEqual("-5", prefix_to_postfix("-5"))
        
   

        
        
if __name__ == "__main__":
    unittest.main()
