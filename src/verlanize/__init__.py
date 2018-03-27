# -*- coding: utf-8 -*-
"""
This verlanize french. 
"""

import logging
import re

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

verlan_words = {
    'américain': 'cainri',      
    'arabe': 'reubeu',
    'argent': 'gen-ar',
    'barette': 'retba',
    'bite': 'teub',
    'bizarre': 'zarbi',
    'black': 'keubla',
    'bombe': 'beubon',
    'bouche': 'cheubou',
    'branché': 'chébran',
    'bête': 'teubé',
    'carotter': 'rot-ca',
    'chaud': 'auch',
    'cher': 'reuch',
    'chien': 'iench',
    'choper': 'pécho',
    'cigarette': 'garetci',
    'cité': 'téci',
    'comme ça': 'ça kom',
    'dingue': 'gueudin',
    'disque': 'skeud',
    'défoncé': 'fonsdé',
    'énervé': 'vénèr',
    'femme': 'meuf',
    'flasher': 'chéfla',
    'flic': 'keuf',
    'fou': 'ouf',
    'français': 'céfran',
    'frère': 'reuf',
    'fumer': 'méfu',
    'fête': 'teuf',
    'gentil': 'tigen',
    'gramme': 'meug',
    'grave': 'veugra',
    'herbe': 'beuh',
    'je ne sais pas': 'Ché ap',
    'joint': 'oinj',
    'juif': 'feuj',
    'louche': 'cheulou',
    'lourd': 'relou',
    'manger': 'géman',
    'mate': 'téma',
    'mater': 'téma',
    'mec': 'keum',
    'merde': 'deumer',
    'moche': 'cheum',
    'moi': 'wam',
    'monnaie': 'némo',
    'mouche': 'cheumou',
    'musique': 'zicmu',
    'mère': 'reum',
    'méchant': 'chan-mé',
    'métro': 'tromé',
    'nez': 'zen',
    'noir': 'renoi',
    'pakistanais': 'kospa',
    'pakos': 'kospa',
    'parents': 'rempa',
    'petit': 'tipeu',
    'photo': 'tofo',
    'pied': 'ièp',
    'pompes': 'peupon',
    'pourri': 'ripou',
    'pute': 'teupu',
    'père': 'reup',
    'pétard': 'tarpé',
    'pétasse': 'tasspé',
    'rage': 'geura',
    'rap': 'peura',
    'ricain': 'cainri',
    'rigoler': 'golri',
    'sec': 'keussé',
    'sein': 'eins',
    'shit': 'teuch',
    'soeur': 'reus',
    'soirée': 'réssoi',
    'toi': 'wat',
    'toubab': 'babtou',
    'triper': 'pétri',
    'truc': 'keutru',
    'vas-y': 'ziva',
    'voiture': 'turvoi',
}



def verlanize(text):
    if text is None:
        return (None, [])
    verlanized = []
    temp = text
    for word in verlan_words:
        pattern = u'\(?' + word + '[\s,.!?;)]?'
        LOGGER.debug("regexp: %s", pattern)
        prog = re.compile(pattern, re.IGNORECASE)
        result = prog.match(temp)
        if prog.match(temp):
            verlanized.append(word)
            temp = prog.sub(verlan_words[word], temp)
    return [temp, verlanized]
