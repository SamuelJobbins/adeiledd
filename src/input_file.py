#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################


"""
input_file.py

Input file parameters for the Adeiledd structure and property prediction suite

Written by Dr Samuel A Jobbins
"""


##############################################################################

##############################################################################
#                            Atomic configuration                            #
##############################################################################


# The Number of Generations for Adeiledd to build and run
# (int)

number_of_generations = 1


# A dictionary containing the atom types to be used in Adeiledd
#
# The keys of the dictionary correspond to the symbols of the elements used
# in the random structure (string)
#
# The values of the dictionary correspond to the number of each atomic species
# to be used in the random structure (int or float) For a random number
# between 1 and 10, choose -1. For a random amount of atom types but enforcing
# some sort of ratio (i.e.. for stoichiometry), use floating point numbers
# between 0 and 1 (the total must equal 1). For example:
#
# atomic_species = {'C' : 2}
# will generate two random atoms of carbon
#
# atomic_species = {'C' : -1}
# will generate a random number of carbon atoms, controlled by the bounds
# min_n_atoms and max_n_atoms
#
# atomic_species = {'Na' : 2, 'Cl' : 2}
# will generate two random atoms of sodium and two random atoms of chlorine
#
# atomic_species = {'Na' : 2, 'Cl' : -1}
# will generate two random atoms of sodium and a random number of chlorine,
# obeying the bounds min_n_atoms and max_n_atoms
#
# atomic_species = {'Na' : -1, 'Cl' : -1}
# will generate a random number of sodium and a random number of chlorine,
# obeying the bounds min_n_atoms and max_n_atoms
#
# atomic_species = {'Na' : 0.5, 'Cl' : 0.5}
# will generate a system with a random number of atoms (bound by min_n_atoms
# and max_n_atoms), and divide them between Na and Cl in a 50:50 ratio
#
# atomic_species = {'Mg' : 0.33, 'Cl' : 0.67}
# will generate a system with a random number of atoms (bound by min_n_atoms
# and max_n_atoms), and divide them between Mg and Cl in a 67:33 ratio. If
# n is odd, floor division will be used, which can sometime affect
# stoichiometry. To enforce an even n, see below.
#
# (dictionary)

atomic_species = {'C' : 4}


# The minimum number of atoms allowed in the simulation cell
# Only used if -1 or floating point number is present in atomic_species.values
# (int)

min_n_atoms = 1


# The maximum number of atoms allowed in the simulation cell
# Only used if -1 or floating point number is present in atomic_species.values
# (int)

max_n_atoms = 12


# Enforce an even number of atoms in the unit cell
# Only used if -1 or floating point number is present in atomic_species.values
# (bool)

enforce_even_n_atoms = True


# An "ideal" bond length between atoms in the system, in Angstrom, to generate
# the initial configuration

equilibrium_bond_length = 1.54


##############################################################################

##############################################################################
#                              DFT configuration                             #
##############################################################################


# Whether or not to perform geometry optimisation using DFT
# (bool)

dft_geometry_optimisation = True


# Calculate the band structure of the material using DFT
# (bool)

dft_band_structure = False


# Calculate the phonon spectrum of the material using DFT
# (bool)

dft_phonon_spectrum = False


##############################################################################

##############################################################################
#                              MM configuration                              #
##############################################################################



# Whether or not to perform geometry optimisation using MM
# (bool)

mm_geometry_optimisation = True



# Calculate the phonon spectrum of the material using MM
# (bool)

mm_phonon_spectrum = False



##############################################################################

##############################################################################
#                            Extras configuration                            #
##############################################################################


# Calculate the thermoelectric figure of merit (zT) of the material
# (bool)

dft_thermoelectric_figure_of_merit = False



# Calculate the superconducting critical temperature (Tc) of the material
# (bool)

dft_superconducting_critical_temperature = False



##############################################################################

##############################################################################
#                            Siesta configuration                            #
##############################################################################


# The path to the siesta executable
# (string)

siesta_path = 'siesta'


# A dictionary of the parameters to use when constructing the siesta input
# files. The keys correspond to the input file flag, and the values their
# values - both should be in string format.
# If you add more, make sure they correspond exactly to the variables used in
# the siesta input file!
# (dictionary)

siesta_variables = {'XC.functional' : 'GGA',
                    'XC.authors' : 'PBE',
                    'MeshCutoff' : '250 Ry',
                    'HarrisFunctional' : '.false.',
                    'MD.MaxForceTol' : '0.075 eV/Ang',
                    'MD.MaxStressTol' : '0.5 GPa',
                    'MD.VariableCell' : '.true.',
                    'MD.ConstantVolume' : '.false.',
                    'MD.UseSaveXV' : '.true.',
                    'MD.UseSaveCG' : '.true.',
                    'SpinPolarized' : '.false.',
                    'PAO.SplitNorm' : '0.15',
                    'PAO.EnergyShift' : '0.005 Ry',
                    'MaxSCFIterations' : '500',
                    'DM.MixingWeight' : '0.12',
                    'DM.Tolerance' : '1.d-4',
                    'DM.NumberPulay' : '5',
                    'SolutionMethod' : 'diagon',
                    'ElectronicTemp' : '298 K',
                    'MD.NumCGsteps' : '500',
                    'UseSaveData' : '.true.',
                    'DM.UseSaveDM' : '.true.',
                    'MD.UseStructFile' : '.false.',
                    'WriteMDXmol' : '.true.',
                    'AtomicCoordinatesFormat' : 'ScaledCartesian',
                    'AtomicCoorFormatOut' : 'Ang',
                    'LatticeConstant' : '1.00 Ang',
                    'KgridCutoff' : '5.0 Ang'}


##############################################################################

##############################################################################
#                             GULP configuration                             #
##############################################################################


# The path to the gulp executable
# (string)

gulp_path = 'gulp'


##############################################################################