#!/usr/bin/python

import sys
import argparse
import os
from math import sqrt

def main(arg):
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', nargs='+', help="xtbopt.xyz file")
	args, unknown = parser.parse_known_args()
	files = args.file 

	if (len(arg) < 1) or (not files):
		sys.exit('At least one argument is required. Only "xtbopt.xyz" supported. Use the option -f to read from a particular file.')

	elements_in_chain = 26
	number_of_chains = 0

	for i in files:
		print('\033[4m' + i + '\033[0m')
		with open(files[0]) as file: 
			lines = file.read().splitlines()
			number_of_chains = (int(lines[0])/elements_in_chain) - 1
		
		first_O_line = 2
		for i in range(number_of_chains):
			second_O_line = first_O_line + 1
			first_H_line = first_O_line + 41
			second_H_line = first_O_line + 42

			values_O1 = lines[first_O_line].strip().split()
			values_O2 = lines[second_O_line].strip().split()
			values_H1 = lines[first_H_line].strip().split()
			values_H2 = lines[second_H_line].strip().split()

			O1X = float(values_O1[1])
			O1Y = float(values_O1[2])
			O1Z = float(values_O1[3])
			O2X = float(values_O2[1])
			O2Y = float(values_O2[2])
			O2Z = float(values_O2[3])
			H1X = float(values_H1[1])
			H1Y = float(values_H1[2])
			H1Z = float(values_H1[3])
			H2X = float(values_H2[1])
			H2Y = float(values_H2[2])
			H2Z = float(values_H2[3])

			print(sqrt((O1X - H1X)**2 + (O1Y - H1Y)**2 + (O1Z - H1Z)**2))
			print(sqrt((O2X - H2X)**2 + (O2Y - H2Y)**2 + (O2Z - H2Z)**2))
			print('')	

			first_O_line += elements_in_chain

if __name__ == '__main__':
	main(sys.argv[1:])