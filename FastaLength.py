import sys
import os
import subprocess

import subprocess
import glob

from Bio import SeqIO

# os.chdir("/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_W22")
# touch="touch WFullTElength_notsd"
# os.system(touch)
#
# FastaFile = open("/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_W22/W22_Genome.fna", 'rU')
# Out=open("/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/FullTElength_notsd", 'r+')
# for rec in SeqIO.parse(FastaFile, 'fasta'):
#     name = rec.id
#     print(name)
#     seq = rec.seq
#     seqLen = len(rec)
#
#     line=name+" "+ str(seqLen)+"\n"
#     Out.(line)
#
# FastaFile.close()
# Out.close()

def extractChromosome(Folder,Genome):
    os.chdir(Folder)
    records = list(SeqIO.parse(Genome, "fasta"))
    for i in range(0,len(records)):
        name=records[i].id
        seq=records[i].seq
        print (name+":"+" "+str(len(seq)))
        entry=name[3:]
        print(entry)
        if(name[0:3]!="Chr"):
            continue
        touch = "touch %s.fasta" % (entry)
        os.system(touch)
        Out = open("%s.fasta" % (entry), 'r+')
        Out.write(">"+str(entry)+" "+str(name)+" " +"\n"+str(seq)+"\n")
        Out.close()


extractChromosome("/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_CML247/","CML247_3.genome.fasta")
