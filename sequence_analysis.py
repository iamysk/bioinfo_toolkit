
# ONE HOT Encoding of DNA sequences
def onehotEncode(sequence):
    # define universe of possible input values
    bases = 'ATGC'
    # define a mapping of chars to integers
    char_to_int = dict((c, i) for i, c in enumerate(bases))
    int_to_char = dict((i, c) for i, c in enumerate(bases))
    # integer encode input data
    integer_encoded = [char_to_int[char] for char in sequence]
    # one hot encode
    onehot_encoded = list()
    for value in integer_encoded:
        letter = [0 for _ in range(len(bases))]
        letter[value] = 1
        onehot_encoded.append(letter)
    #return list(map(list, zip(*onehot_encoded)))
    return(onehot_encoded)

# Function to extract fasta from bed file
import os
def bed2fasta(refpath, bedpath, outpath):
	for file_ in os.listdir(bedpath):
		cmd = "bedtools getfasta -fi %s -bed %s -fo %s"%(refpath, bedpath+file_, outpath+file_.split('.')[0]+'.fa')
		os.system(cmd)