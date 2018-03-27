'''
Created on Mar 27, 2018

@author: pivi
'''    
import unittest
import logging
import verlanize

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

class TestVerlanizeCase(unittest.TestCase):

    def test_none(self):
        result, words = verlanize.verlanize(None)
        self.assertIsNone(result)
        self.assertIsNotNone(words)
        self.assertEquals(0, len(words))
        
    def test_simple_word(self):
        result, words = verlanize.verlanize('femme')
        self.assertIsNotNone(result)
        self.assertIsNotNone(words)
        self.assertEqual('meuf', result)
        self.assertEqual(1, len(words))
        
    def test_accent_word(self):
        result, words = verlanize.verlanize('pétard')
        self.assertIsNotNone(result)
        self.assertIsNotNone(words)
        self.assertEqual('tarpé', result)
        self.assertEqual(1, len(words))
        
#     def test_upcase_word(self):
#         result, words = verlanize.verlanize('FEMME')
#         self.assertIsNotNone(result)
#         self.assertIsNotNone(words)
#         self.assertEqual('MEUF', result)
#         self.assertEqual(1, len(words))
     

if __name__ == '__main__':
    unittest.main()