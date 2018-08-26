# -*- coding: utf-8 -*-
'''
Created on Mar 27, 2018

@author: pivi
'''
import logging
import unittest

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

    def test_same_words(self):
        result, words = verlanize.verlanize('femme femme, femme. femme; '
                                            'femme? femme! '
                                            '(femme) (femme femme)')
        self.assertIsNotNone(result)
        self.assertIsNotNone(words)
        self.assertEqual('meuf meuf, meuf. meuf; '
                         'meuf? meuf! (meuf) '
                         '(meuf meuf)', result)
        self.assertEqual(9, len(words))

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

    def test_simple_word_with_matcher(self):

        def matcher(match, verlan, x_sampa):
            return ''.join([match.string[:match.start()],
                            'X_SAMPA',
                            match.string[match.end():]])

        result, words = verlanize.verlanize('Un américain à Paris', matcher)
        self.assertIsNotNone(result)
        self.assertIsNotNone(words)
        self.assertEqual('Un X_SAMPA à Paris', result)
        self.assertEqual(1, len(words))

    def test_expr_title(self):
        result, words = verlanize.verlanize('Je ne sais pas comment te dire')
        self.assertIsNotNone(result)
        self.assertIsNotNone(words)
        self.assertEqual('Ché ap comment te dire', result)
        self.assertEqual(1, len(words))

    def test_expr_normal(self):
        result, words = verlanize.verlanize('Et bien, je ne sais pas comment te dire')
        self.assertIsNotNone(result)
        self.assertIsNotNone(words)
        self.assertEqual('Et bien, ché ap comment te dire', result)
        self.assertEqual(1, len(words))

    def test_long_test(self):
        N = 1000
        txt = "Un américain, un autre américain, un arabe et un planqué vont à Paris. " * N
        result, words = verlanize.verlanize(txt)
        self.assertIsNotNone(result)
        self.assertIsNotNone(words)
        self.assertEqual('Un cainri, un autre cainri, un rebeu et un képlan vont à Paris. ' * N, result)
        self.assertEqual(4 * N, len(words))

# TODO: implement this use case
#     def test_voyel_conson_normal(self):
#         result, words = verlanize.verlanize("L'américain à Paris")
#         self.assertIsNotNone(result)
#         self.assertIsNotNone(words)
#         self.assertEqual('Le cainri à Paris', result)
#         self.assertEqual(1, len(words))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
