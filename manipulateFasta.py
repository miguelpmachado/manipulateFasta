#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
getSeqENA.py - Get fastq files from ENA using Run IDs
<https://github.com/miguelpmachado/manipulateFasta/>

Copyright (C) 2016 Miguel Machado <mpmachado@medicina.ulisboa.pt>

Last modified: July 15, 2016

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import argparse
import sys
from getSequences import getSequences


def runGetSequences(args):
	print '\n' + 'Getting sequences...'

	fastaFile = args.gsFasta[0].name
	listFile = args.gsList[0].name
	outputFile = args.gsOutFile[0]

	outputFile, number_sequences, number_bases = getSequences(fastaFile, listFile, outputFile)

	print str(number_bases) + ' bases were retreived in ' + str(number_sequences) + ' sequences'
	print 'And stored in ' + outputFile

	if number_sequences == 0:
		sys.exit('It was not possible to retreive any sequence!')


def main():

	parser = argparse.ArgumentParser(prog='manipulateFasta.py', description="Manipulate FASTA files", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--version', help='Version information', action='version', version=str('%(prog)s v0.1'))
	subparsers = parser.add_subparsers()

	# getSequences
	parser_getSequences = subparsers.add_parser('getSequences', description="Retreive sequences from a FASTA file", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	getSequences_required = parser_getSequences.add_argument_group('getSequences required options')
	getSequences_required.add_argument('--gsFasta', nargs=1, type=argparse.FileType('r'), metavar='/path/to/fasta/file.fa', help='Path to FASTA file', required=True)
	getSequences_required.add_argument('--gsList', nargs=1, type=argparse.FileType('r'), metavar='/path/to/sequences/list.txt', help='Path to file containing the list of sequences to download', required=True)
	getSequences_required.add_argument('--gsOutFile', nargs=1, type=str, metavar='/output/fasta/file.fa', help='Where to store the output fasta file', required=True)

	parser_getSequences.set_defaults(func=runGetSequences)

	args = parser.parse_args()

	args.func(args)


if __name__ == "__main__":
	main()
