# -*- coding: utf-8 -*-
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

    @classmethod
    def setUpClass(cls):
        verlanize.init()

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
    
    def test_simple_sentence(self):
        result, words = verlanize.verlanize('Une femme jolie.')
        self.assertIsNotNone(result)
        self.assertIsNotNone(words)
        self.assertEqual('Une meuf jolie.', result)
        self.assertEqual(1, len(words))
      
    def test_many_words(self):
        result, words = verlanize.verlanize('pétard planqué')
        self.assertIsNotNone(result)
        self.assertIsNotNone(words)
        self.assertEqual('tarpé képlan', result)
        self.assertEqual(2, len(words))
    
    def test_simple_sentence_many_words(self):
        result, words = verlanize.verlanize('Un pétard mouillé.')
        self.assertIsNotNone(result)
        self.assertIsNotNone(words)
        self.assertEqual('Un tarpé yémou.', result)
        self.assertEqual(2, len(words))
    
    def test_upcase_word(self):
        result, words = verlanize.verlanize('FEMME')
        self.assertIsNotNone(result)
        self.assertIsNotNone(words)
        self.assertEqual('MEUF', result)
        self.assertEqual(1, len(words))
     

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()