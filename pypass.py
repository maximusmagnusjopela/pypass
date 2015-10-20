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
    print(args)
    return

def genpass(alphabet,length):
    """Returns a secure random password

    :alphabet: sequence of symbols to use in password generation
    :length: lenght of the password
    :returns: a sequence of randomly picked symbols

    """

    password = "".join([random.choice(alphabet) for _ in range(length)])
    return password

def menmonic(password):
    """Returns a mnemonic, a human friendly bag of words, that helps remember
    the password.

    :password: collection of symbols for the mnemonic
    :returns: mnemonic

    """

    # lowercase == NATO Phonetic Alphabet,
    # uppercase == Western Union Phonetic Alphabet
    # ref : http://www.osric.com/chris/phonetic.html

    return






if __name__ == '__main__':
    main()

