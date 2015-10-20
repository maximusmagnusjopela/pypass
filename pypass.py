#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import string

from Crypto.Random import random

def main():
    """ Crypto secure pwd generator in python
    :returns: TODO

    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-l',
            '--length',
            type=int,
            help='length of the generated password',
            default=8
            )

    parser.add_argument(
            '-a',
            '--alphabet',
            help='sequence of symbols to use in password generation',
            default=string.ascii_letters + '0123456789',
            )

    parser.add_argument(
            '-m',
            '--mnemonic',
            help='prints a human friendly mnemonic that helps remember the'\
                    ' generated password',
            action='store_true',
            default=False
            )

    args = parser.parse_args()

    password = genpass(args.alphabet, args.length)
    print(password)

    if args.mnemonic:
        print(mnemonic(password))

    return

def genpass(alphabet,length):
    """Returns a secure random password

    :alphabet: sequence of symbols to use in password generation
    :length: lenght of the password
    :returns: a sequence of randomly picked symbols

    """

    password = "".join([random.choice(alphabet) for _ in range(length)])
    return password

def mnemonic(password):
    """Returns a mnemonic, a human friendly bag of words, that helps remember
    the password.

    :password: collection of symbols for the mnemonic
    :returns: mnemonic

    """

    # lowercase == NATO Phonetic Alphabet,
    # uppercase == Western Union Phonetic Alphabet + modif to solve conflicts
    # ref : http://www.osric.com/chris/phonetic.html
    mapping = {
        'a':'Alpha',
        'b':'Bravo',
        'c':'Charlie',
        'd':'Delta',
        'e':'Echo',
        'f':'Foxtrot',
        'g':'Golf',
        'h':'Hotel',
        'i':'India',
        'j':'Juliet',
        'k':'Kilo',
        'l':'Lima',
        'm':'Mike',
        'n':'November',
        'o':'Oscar',
        'p':'Papa',
        'q':'Quebec',
        'r':'Romeo',
        's':'Sierra',
        't':'Tango',
        'u':'Uniform',
        'v':'Victor',
        'w':'Whiskey',
        'x':'X-ray',
        'y':'Yankee',
        'z':'Zulu',
        'A':'Adams',
        'B':'Boston',
        'C':'Chicago',
        'D':'Denver',
        'E':'Easy',
        'F':'Frank',
        'G':'George',
        'H':'Henry',
        'I':'Ida',
        'J':'John',
        'K':'King',
        'L':'Lincoln',
        'M':'Mary',
        'N':'New York',
        'O':'Ocean',
        'P':'Peter',
        'Q':'Queen',
        'R':'Roger',
        'S':'Sugar',
        'T':'Thomas',
        'U':'Union',
        'V':'Victor',
        'W':'William',
        'X':'X-file',
        'Y':'Young',
        'Z':'Zeta',
        '0':'Zero',
        '1':'Wun',
        '2':'Too',
        '3':'Tree',
        '4':'Fower',
        '5':'Fife',
        '6':'Six',
        '7':'Seven',
        '8':'Ait',
        '9':'Niner'}

    # if alphabet symbol not found in table, just return it
    result = " ".join([ mapping.get(symbol,symbol) for symbol in password ])
    return result

if __name__ == '__main__':
    main()

