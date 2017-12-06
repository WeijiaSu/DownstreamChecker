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


def getcompleteList(TIDList,noDupList,CList,Folder):
    os.chdir(Folder)
    o=open(CList,'a+')
    for TID in open(TIDList,'r+').readlines():
        for all in  open(noDupList,"r+").readlines():
            if(TID[:-1]==all.split()[1]):
                o.write(all)
                break
    o.close()
# getcompleteList("Maize_chr1_TIDList","/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/DDS2/chr1_noDup","Chr1_Clist","/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/1009/TIDList")

#### Get dupLength from DDS2 file
def getDupLength(file):
    d1={}
    d2={}
    with open(file, "r", encoding='utf-8', errors='ignore') as f:
        lines=f.readlines()
        for i in range(len(lines)):
            columns=lines[i].split()
            FirstStart=columns[1]
            FirstEnd=columns[2]
            length1=int(FirstEnd)-int(FirstStart)+1
            d1[FirstStart]=length1
            SecondStart = columns[5]
            SecondEnd = columns[6]
            length2 = int(SecondEnd) - int(SecondStart) + 1
            d2[FirstStart] = length2

    return d1,d2


d1,d2=getDupLength("/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/1009/TIDList/Chr1_Clist")
print(d1)
list1=[]
for key in d1:
    list1.append(int(key))
    print(int(key))
print(list1)
list2=[]
for i in list1:
    list2.append(d1[str(i)])
    print(d1[str(i)])
print(list2)

# print(getDupLength("/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Rice/Oryza_sativa/DDS2_0812/chr1_1_1HSP"))
# print(len(getDupLength("/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Rice/Oryza_sativa/DDS2_0812/chr1_1_1HSP")))


### rule out duplicated TE cases, and the cases that TE in the middle  of the duplication




# def ClassByTe(Folder,TeLengthFile,DDSfile):
#     os.chdir(Folder)
#     folder = Folder
#     os.system("mkdir TE_Only")
#     os.system("mkdir TE_Terminal")
#     os.system("mkdir TE_Middle")
#
#
#     TElength=GetTeLength(TeLengthFile)
#     Duplength1, Duplength2=getDupLength(DDSfile)
#     for file in os.listdir(folder):
#         path = os.path.join(folder, file)
#         Name=basename(file)
#         # print(Name)
#         FirstStart=Name[:-2]
#         if os.path.isdir(path):
#             # skip directories
#             continue
#         if (os.path.isfile(".DS_Store")):
#             os.remove(".DS_Store")
#             continue
#
#
#
#         with open(file, "r", encoding='utf-8', errors='ignore') as f:
#             CommenTE = GetFirSameTe(file)
#             # print(CommenTE)
#             FirstComTE = CommenTE[Name]
#             # print(FirstComTE)
#             lines = f.readlines()
#             for line in lines:
#                 columns = line.split()
#                 if(columns[1]==FirstComTE):
#                     aligLength = columns[3]
#                     TeName = columns[1]
#                     realTELength = TElength[TeName]
#                     realDuplength = Duplength1[FirstStart]
#                     if (abs(int(realDuplength) - int(aligLength)) < 21):
#                         move = "mv %s TE_Only/" % (file)
#                         os.system(move)
#                         break
#                     elif((int(columns[8])==1) or int(columns[9])==int(realTELength) or int(columns[8])==int(realTELength) or int(columns[9])==1):
#                         move = "mv %s TE_Terminal/" % (file)
#                         os.system(move)
#                         break
#                     else:
#                         move = "mv %s TE_Middle/" % (file)
#                         os.system(move)
#                         break
#             f.close()


# ClassByTE(
#                 "/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize0828/DupBlastTE/2TE/SameTE",
#                 "/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Rice/TElength",
#                 "/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Rice/Oryza_sativa/DDS2_0812/chr2_1HSP")

        #     for i in range(len(lines)):
        #         columns = lines[i].split()
        #         if (columns[1] == FirstComTE):
        #             aligLength = columns[3]
        #             # print(aligLength)
        #             TeName = columns[1]
        #             # print(TeName)
        #
        #             realTELength = TElength[TeName]
        #             # print(realLength)
        #             realDuplength=Duplength[FirstStart]
        #             if (int(realDuplength) - int(aligLength) < 21):
        #                 move = "mv %s TE_Only/" % (file)
        #                 os.system(move)
        #             elif ((int(columns[8]) < 10 or int(columns[9]) > (int(realTELength) - 10)) or (
        #                             int(columns[8]) > (int(realTELength) - 10) or int(columns[9]) < 10)):
        #                 move = "mv %s TE_Terminal/" % (file)
        #                 os.system(move)
        #             else:
        #                 move = "mv %s TE_Middle/" % (file)
        #                 os.system(move)
        # f.close()



#

# organize("/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Rice/Oryza_sativa/DDS2_0812/chr1_mHSP_blast/2TE/SameTE/TE_Terminal")