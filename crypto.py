# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 23:43:18 2022

@author: nmesomav
"""

alphabet = []

for number in range(97,123):
    alphabet.append(chr(number))
    

def Vigenere(msg, cle):
    alphabet = []
    res = ''
    for number in range(97,123):
        alphabet.append(chr(number))
    alpha = ''.join(alphabet)
    i = 0
    for caractere in msg:
        debut = alpha.find(cle[i])
        pos = alpha.find(caractere)
        indice = pos + debut
        if indice > 25 :
            indice -= 26
        res += alpha[indice]
        i +=1
        if i >= len(cle) :
            i = 0
    return res

message = input('Entrez le message: ')
key = input('Enterez la clé: ')
print(Vigenere(message, key))