"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

import unittest

def word_refractoring(word:str):
    if word.isalnum():
        return word[1:] + word[0] + "ay"
    else:
        return word

def pig_it(text:str):
    words = text.split()
    words = list(map(word_refractoring, words))
    words = list(map(lambda x: x + " ", words))
    answ = "".join(words)
    return answ[:len(answ)-1]

class TestCakes(unittest.TestCase):
    def test1(self):
        self.assertEqual(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')

    def test2(self):
        self.assertEqual(pig_it('This is my string'),'hisTay siay ymay tringsay')

    def test3(self):
        self.assertEqual(pig_it('Quis custodiet ipsos custodes ?'),'uisQay ustodietcay psosiay ustodescay ?')
        
unittest.main()

