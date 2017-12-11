import sys
import os
import subprocess
import glob
import sys
import subprocess
import glob
from os.path import basename



def RemoveRedudantEntry(Folder,file,NewFILENAME):
    f = open(file,'r+')
    os.chdir(Folder)
    out = None
    lines = f.readlines()
    length = len(lines)
    touch = "touch %s"%(NewFILENAME)
    os.system(touch)
    count = 1
    list = []
    n = len(list)
    out = open(NewFILENAME, 'a+')
    i = 0
    while (i < len(lines) - 2):
        equali = 0
        columns = lines[i].split()
        Nextcolumns = lines[i + 1].split()
        if (columns[1] == Nextcolumns[1]):
            list.append(lines[i])
            Next2column = lines[i + 2].split()
            if (Nextcolumns[1] != Next2column[1]):
                list.append(lines[i + 1])
                list3 = []
                for j in range(len(list)):
                    c1 = list[j].split()
                    list3.append(int(c1[3]))
                Max = max(list3)
                for k in range(len(list)):
                    c2 = list[k].split()
                    if (int(c2[3]) == Max):
                        out.write(list[k])
                        break
                i = i + 2
                list = []
            elif (i + 2 == len(lines) - 1):
                list.append(lines[len(lines) - 1])
                list.append(lines[len(lines) - 2])
                list3 = []
                for j1 in range(len(list)):
                    cj1 = list[j1].split()
                    list3.append(int(cj1[3]))
                Max = max(list3)
                for k1 in range(len(list)):
                    cj2 = list[k1].split()
                    if (int(cj2[3]) == Max):
                        out.write(list[k1])
                        break
                i = i + 2
                list = []

            else:
                i = i + 1

        else:
            out.write(lines[i])
            i = i + 1
    # if(lines[length-])
    f.close()

#for i in range (1,11):
#     fileneme="/work/LAS/thomasp-lab/weijia/research/Sorghum/"+"Sorghum_chr"+str(i)+"_100k"
#     NewName="Sorghum_chr"+str(i)+"_noDup"
#    RemoveRedudantEntry("/work/LAS/thomasp-lab/weijia/research/Sorghum/",
#                        fileneme,NewName)


RemoveRedudantEntry("/work/LAS/thomasp-lab/weijia/research/Maize_mo17/","/work/LAS/thomasp-lab/weijia/research/Maize_mo17/filter_mo17_chr1.300","nr__mo17_chr1.300")
RemoveRedudantEntry("/work/LAS/thomasp-lab/weijia/research/Maize_mo17/","/work/LAS/thomasp-lab/weijia/research/Maize_mo17/filter_mo17_chr1.30","nr__mo17_chr1.30")
