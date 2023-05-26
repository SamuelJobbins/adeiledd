#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################


"""
generate_random_crystal_structure.py

Generates random crystal structure based on input parameters

Written by Dr Samuel A Jobbins
"""


##############################################################################

from input_file import *

##############################################################################


def read_atomic_species(atomic_species):
    
    atomic_symbols = []
    atomic_numbers = []
    atomic_masses = []
    number_of_atoms = []
    
    for key, value in atomic_species.items():
        
        atomic_symbols.append(key)
        
        if type(value) == int:
            if value == -1:
                pass
            else:
                number_of_atoms.append(value)
        else:
            pass
        
    return atomic_symbols, atomic_numbers, atomic_masses, number_of_atoms
                
        
        
##############################################################################


atomic_symbols, atomic_numbers, atomic_masses, number_of_atoms = \
    read_atomic_species(atomic_species)