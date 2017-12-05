import sys
from Bio import SeqIO
import os
import subprocess
import glob
import sys
from Bio.Blast.Applications import NcbiblastnCommandline
from io import StringIO
from Bio.Blast import NCBIXML
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Blast import NCBIXML
import subprocess
import glob
from os.path import basename
import PIL
from PIL import Image, ImageDraw, ImageFont


# base = Image.open('lena.png').convert('RGBA')
def getTwosetLines(file):
   f=open(file, "r", encoding='utf-8', errors='ignore')
   lines = f.readlines()
   set1 =[]
   set2 =[]
   for i in range(len(lines)):
       columns = lines[i].split()
       if (columns[0] == "#"):
           continue
       if (columns[0] != "#"):
           for j in range(i, len(lines)):
               columnsj = lines[j].split()
               if (columnsj[0] != "#"):
                   set1.append(columnsj)
                   i = i + 1
               if (columnsj[0] == "#"):
                   i = i + 1
                   break
           for k in range(i, len(lines)):
                   columns = lines[i].split()
                   if(columns[0]=="#"):
                       i=i+1
                       continue
                   else:
                       columnsk = lines[k].split()
                       if (columnsk[0] != "#"):
                           set2.append(columnsk)
                           i = i + 1
                       if (columnsk[0] == "#"):
                           i = i + 1
                           break

           break
       break

   return set1,set2

def setgraphsize(file):
    TE,Dup=getTwosetLines(file)
    TEcolumn=TE[0]
    Dupcolumn=Dup[0]
    whole=int(TEcolumn[3])+int(Dupcolumn[3])
    print(whole)
    if(whole<500):
        im = Image.new('RGBA', (500, 500))
        draw = ImageDraw.Draw(im)
        perTE=int(TEcolumn[3])/whole
        lenTE=perTE*200
        print(perTE)
        perDup=int(Dupcolumn[3])/whole
        lenDup=perDup*200
        print(perDup)
        # draw.line((50, 200, 350, 200), fill="black", width=3)
        draw.line((50, 300, 50+lenTE, 300), fill="red", width=20)
        draw.line((50+lenTE, 300, 50+lenTE+lenDup, 300), fill="blue", width=20)
        draw.line((50+lenTE+lenDup, 300, 50+2*lenTE+lenDup, 300), fill="red", width=20)
        draw.line((50+2*lenTE+lenDup, 300, 50+2*lenTE+2*lenDup, 300), fill="blue", width=20)
        del draw
        im.show()
    # write to stdout
        im.save("test.png")


setgraphsize("/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Rice/Oryza_sativa/chr1_DupBlastTE/2TE/SameTE/TE_Terminal/finalresult/C12496162_Ind")




# draw.polygon([(100,200),(100,300),(300,200),(300,300)], outline="red",fill="red")
# draw.line((0, im.size[1], im.size[0], 0), fill=128)



