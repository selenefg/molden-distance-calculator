#!/usr/bin/python

#raiz de   (ox-hx)^2 + (oy-hy)^2 + (oz-hz)^2

import sys
import argparse

def main(arg):
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', nargs='+', help="xtbopt.xyz file")
	args, unknown = parser.parse_known_args()
	files = args.file 

	elements_in_chain = 26
	number_of_chains = 0

	for i in files:
		print("\033[4m" + i + "\033[0m")
		with open(files[0]) as file: 
			lines = file.read().splitlines()
			number_of_chains = (int(lines[0])/elements_in_chain) - 1
		
		first_O_line = 2
		for i in range(number_of_chains):
			second_O_line = first_O_line + 1
			first_H_line = first_O_line + 41
			second_H_line = first_O_line + 42

			print(lines[first_O_line])
			print(lines[second_O_line])
			print(lines[first_H_line])
			print(lines[second_H_line])
			print('')	

			first_O_line += elements_in_chain

if __name__ == '__main__':
	main(sys.argv)