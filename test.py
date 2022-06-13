import unittest
from is_prime import *
class Test(unittest.TestCase):
    def test_1(self):
        ''' Test that 2 is not prime number'''
        self.assertFalse(is_prime(2))


    def test_4(self):
        ''' Test that 4 is not prime number'''
        self.assertFalse(is_prime(4))

    def test_5(self):
        ''' Test that 5 is not prime number'''
        self.assertTrue(is_prime(5))         
    def test_25(self):
        ''' Test that 25 is not prime number'''
        self.assertFalse(is_prime(25))         


if __name__ =="__main__":
    unittest.main()       