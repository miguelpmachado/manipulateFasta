import os


def setOutFile(outputFile):
	outputFile = os.path.abspath(outputFile)
	if not os.path.isdir(os.path.dirname(outputFile)):
		os.makedirs(os.path.dirname(outputFile))
	return outputFile


def getListSequences(sequencesListFile):
	list_sequences = []
	with open(sequencesListFile, 'rtU') as lines:
		for line in lines:
			line = line.splitlines()[0]
			if len(line) > 0:
				if line[0] == '>':
					line = line[1:]
				list_sequences.append(line)
	return list_sequences


def writeOutFile(fastaFile, list_sequences, outputFile):
	writer = open(outputFile, 'wt')

	number_sequences = 0
	number_bases = 0
	seqHeader = ''
	seqSequence = ''
	with open(fastaFile, 'rtU') as lines:
		for line in lines:
			line = line.splitlines()[0]
			if len(line) > 0:
				if line[0] == '>':
					if seqHeader != '':
						if seqHeader[1:] in list_sequences:
							writer.write(seqHeader + '\n')
							writer.write(seqSequence + '\n')
							writer.flush()
							number_bases = number_bases + len(seqSequence)
							number_sequences += 1
					seqHeader = ''
					seqSequence = ''
					seqHeader = line
				else:
					seqSequence = seqSequence + line
		if seqHeader[1:] in list_sequences:
			writer.write(seqHeader + '\n')
			writer.write(seqSequence + '\n')
			writer.flush()
			number_bases = number_bases + len(seqSequence)
			number_sequences += 1

	writer.close()

	return number_sequences, number_bases


def getSequences(fastaFile, sequencesListFile, outputFile):
	outputFile = setOutFile(outputFile)

	list_sequences = getListSequences(sequencesListFile)

	number_sequences, number_bases = writeOutFile(fastaFile, list_sequences, outputFile)

	return outputFile, number_sequences, number_bases
