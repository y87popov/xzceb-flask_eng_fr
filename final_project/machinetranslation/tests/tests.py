import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
 def test1(self): 
   
      # Test Bonjour returns Hello

     self.assertEqual(english_to_french('Hello'), 'Bonjour')

        # Test Bonjour does not return Bonjour

     self.assertNotEqual(english_to_french('Hello'), 'Hello')
     
 unittest.main()
