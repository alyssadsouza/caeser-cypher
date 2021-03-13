# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 19:56:24 2020

@author: Alyssa
"""

def CaesarCypher(code, shift):
    '''
    Parameters
    ----------
    code : str
            Contains a message to be encrypted, or that is already encrypted, using the Caesar Cypher.
    shift : int
            Number of letters to shift message over.

    Returns
    -------
    String of encrypted/decrypted message.

    '''
    import string

    str1 = string.ascii_lowercase
    str2 = str1[shift:] + str1[:shift]

    t = code.maketrans(str1, str2)
    message = ''
    
    for letter in code:
        if letter.isalpha():
            for key in t.keys():
                if letter == chr(key):
                    message += chr(t[key])
        else:
            message += letter
        
    return message
