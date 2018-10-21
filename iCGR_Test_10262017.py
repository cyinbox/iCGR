# The use case of integer chaos game (iCGR) encoding and decoding DNA sequences
#
# Changchuan Yin, Ph.D.
# Dept. of Mathematics, Statistics and Computer Science
# University of Illinois at Chicago
# Chicago, IL 60607
# USA
#
# Email cyin1@uic.edu, cyinbox@gmail.com
# Last update 10/26/2017
#
# Citation
# Yin, C.(2018). Encoding DNA sequences by integer chaos game representation. Journal of Computational Biology.


import iCGR 

#Homo sapiens SMPX gene for alternative protein SMPX, isolate 15610, GenBank: HF583935.1
#https://www.ncbi.nlm.nih.gov/nuccore/HF583935.1?report=fasta
DNASeq = 'ATGGAGAATGATATGGCAATGTGCCTAACGATTTTGATGAAAAGTTTCCCAAGCTACTTCCTACAGTATT'
print('Original DNA sequence:', DNASeq)

# 1. Encoding DNA sequence by integer CGR (iCGR)
x_n,y_n,n = iCGR.encodeDNASequence(DNASeq)
print('Encoded tri-integers:', x_n, y_n, n)

# 2. Decoding DNA sequence from tri-integers
DNAseq_decoded = iCGR.decodeDNASequence(x_n, y_n, n)
print('Decoded DNA sequence:', DNAseq_decoded)

if DNASeq == DNAseq_decoded:
    print('Successfully encoding and decoding by iCGR.')
else:
    print('Unsuccessfully encoding and decoding.')

