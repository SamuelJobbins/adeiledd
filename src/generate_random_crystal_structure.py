#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################


"""
generate_random_crystal_structure.py

Generates random crystal structure based on input parameters

Written by Dr Samuel A Jobbins
"""


##############################################################################

import numpy as np
import pandas as pd
import random

from input_file import *

##############################################################################


def read_pub_chem_elements(pub_chem_elements_file):
    df = pd.read_csv(pub_chem_elements_file)
    return df


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
                print('At the moment, only integer atom counts are permitted')
                exit
            else:
                number_of_atoms.append(value)
        else:
            print('At the moment, only integer atom counts are permitted')
            exit
    
        atomic_numbers.append(pub_chem_elements['AtomicNumber'][
            pub_chem_elements['Symbol'] == key].values[0])
    
        atomic_masses.append(pub_chem_elements['AtomicMass'][
            pub_chem_elements['Symbol'] == key].values[0])
        
    return atomic_symbols, atomic_numbers, atomic_masses, number_of_atoms

        
##############################################################################


def build_random_configuration(atomic_symbols,
                               number_of_atoms, spacing_function=''):
    
    spacing_function = (
            (equilibrium_bond_length ** 3) * sum(number_of_atoms)) ** (1/3) + 1
    
    for index, atom_symbol in enumerate(atomic_symbols):
        for atom in range(number_of_atoms[index]):
            x = random.uniform(equilibrium_bond_length/4,
                               spacing_function - equilibrium_bond_length/4)
            y = random.uniform(equilibrium_bond_length/4,
                               spacing_function - equilibrium_bond_length/4)
            z = random.uniform(equilibrium_bond_length/4,
                               spacing_function - equilibrium_bond_length/4)
            print(f'{atom_symbol}{x}{y}{z}')
        
    
a = np.array([0.5, 0.5, 0.5])
b = np.array([[2.5, 1, 0],[0, 2.5, 0],[2, 0, 2.5]]) 
np.matmul(a, b)


##############################################################################

pub_chem_elements = read_pub_chem_elements('pub_chem_elements_all.csv')

atomic_symbols, atomic_numbers, atomic_masses, number_of_atoms = \
    read_atomic_species(atomic_species)
    
build_random_configuration(atomic_symbols, number_of_atoms)