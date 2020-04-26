# molden-distance-calculator
The simple program to calculate **Hydrogen Bonds**

The program Molden (by Gijs Schaftenaar, at the Centre for Molecular and Biomolecular Informatics) is a program used to visualize the results of quantum chemical calculations. This program uses a "Calculate" function which measures distances, bond angles and dihedral angles in diferent structures. The distance measurement is particularly valuable, it can be used to monitor the development of a bond distance along a reaction pathway or other sequence of multiple structures.

The problem with this tool is that there isn't an option to calculate this measurements in batch. You have to click on them one by one. The intention of this script is to help automate the distance calculating process.

In particular, we will be calculating hydrogen bonds.

The supported input file format is "xtbopt.xyz".
