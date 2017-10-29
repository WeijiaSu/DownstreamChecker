import sys
import os
import subprocess
import glob
import sys
import subprocess
import glob
from os.path import basename



for i in range(1,11):
    os.chdir("/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_CML247/")
    copy = "cp DDS Maize_CML247_chr%s" % (i)
    os.system(copy)
    f = open("Maize_CML247_chr%s" % (i), 'a+')
    f.write("#SBATCH --job-name='CML247_chr%s'"%(i)+"\n")
    f.write("#SBATCH --output='CML247_chr%s'"%(i) +" "+ "# job standard output file (%j replaced by job id)"+"\n")
    f.write("#SBATCH --error='CML247_chr%s'"%(i) +" "+ "# job standard output file (%j replaced by job id)"+"\n")
    f.write("#"+"\n"+"#LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE"+"\n"+"#"+"\n"+"#"+"\n"+"\n")

    f.write("/home/weijia/research/DDS2/dds2"+" "+"/work/LAS/thomasp-lab/weijia/research/MaizeGenome/Maize_CML247/%s.fasta"%(i)+" "+
            "/work/LAS/thomasp-lab/weijia/research/MaizeGenome/Maize_CML247/%s.fasta"%(i)+" "+"-a 30 -i 100 -f 200 -n 2 -p 90 -x 300 -y 300 -r 30"
            +" "+">"+" "+"CML247_chr%s.dds2"%(i)+"\n")
    f.write("grep Chain CML247_chr%s.dds2 | sort -k 2 -n > CML247_chr%s.dds2.sort"%(i,i))
    f.close()


    # folderName="DDS_Maize_chr"+str(i)+"_noDup"
    # f.write('folderName="DDS_Maize_chr"+str(%s)+"_noDup"' % (i) + "\n")
    # f.write("mk = 'mkdir %s'" % (folderName)+ "\n")
    # f.write("os.system(mk)"+'\n')
    # Dupfile = "/work/LAS/thomasp-lab/weijia/research/0926RepDB/Maize/chr" + str(i) + "_noDup"
    # entry = i
    # Folder = "/work/LAS/thomasp-lab/weijia/research/Maize_DDSTE/" + folderName
    # ncbi="chr"+str(i)+"ncbi/"
    # Database='/work/LAS/thomasp-lab/weijia/research/0926RepDB/Maize/Maize_Nodup/'+ncbi+"Zea_mays.AGPv4.dna.chromosome.%s.fa"%(i)
    # f.write("DupBlastTE('%s','%s',%s, '/work/LAS/thomasp-lab/weijia/research/0926RepDB/Maize/Maize_Nodup/22_maize_seed_noTSD.fa','%s')"%(Dupfile,Database,entry, Folder))
    f.close()


##################################################################
    # copy = "cp Maize.py mo17_Fulldb_chr_%s.py" % (i)
    # os.system(copy)
    # f = open("mo17_Fulldb_chr_%s.py" % (i), 'a+')
    # folderName = "mo17_chr_" + str(i) + "_Fulldb"
    # f.write('folderName="%s"' % (folderName) + "\n")
    # f.write("mk = 'mkdir %s'" % (folderName) + "\n")
    # f.write("os.system(mk)" + '\n')
    # Dupfile = "/work/LAS/thomasp-lab/weijia/research/Maize_mo17/noDup/" + "mo17_chr%s_noDup"%(i)
    # entry = i
    # Folder = "/work/LAS/thomasp-lab/weijia/research/Maize_mo17/noDup/" + folderName
    # # ncbi = "chr" + str(i) + "ncbi/"
    # Database = '/work/LAS/thomasp-lab/weijia/research/Maize_mo17/ncbi/mo17.fasta'
    # TEbase="/work/LAS/thomasp-lab/weijia/research/0926RepDB/Maize/Maize_Nodup/maizeTEdb.fa"
    # f.write(
    #     "DupBlastTE('%s','%s',%s, '%s','%s')" % (
    #     Dupfile, Database, entry,TEbase, Folder))
    #
    # f.close()
######################################################################
    # copy="cp PBS PBS_mo17_chr_%s"%(i)
    # os.system(copy)
    # f=open("PBS_mo17_chr_%s"%(i),'a+')
    # # copy = "cp BlastDupTE.py Blast_dupTE_%s.py" % (i)
    # # os.system(copy)
    # fileName="mo17_Fulldb_chr_%s.py"%(i)
    # f.write('python %s'%(fileName))




def RemoveRedudantEntry(Folder, file, NewFILENAME):
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

# for i in range (1,11):
#     fileneme="/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_mo17/noDup/"+"mo17_chr"+str(i)+"_100k"
#     NewName="mo17_chr"+str(i)+"_noDup"
#     RemoveRedudantEntry("/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_mo17/noDup",
#                         fileneme,NewName)


def checkTID(Folder,outfoder,ddsFILE,outfilename):
    os.chdir(Folder)
    OUT=open("%s"%(outfilename),'a+')
    os.chdir(outfoder)
    folder = outfoder
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        Name=basename(file)
        FirstStart = Name[:-2]
        f=open(ddsFILE,'r+')
        lines=f.readlines()
        for line in lines:
            columns=line.split()
            if (FirstStart==columns[1]):
                OUT.write(line)


for i in range(1,11):
    Folder="/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/1009/Maize_chr%sFulldb/SameTE/"%(i)
    E=str(Folder)+"Exception/"
    TE_Middle=str(Folder)+"TE_Middle/"
    TE_Terminal=str(Folder)+"TE_Terminal/"
    ddsFIle="/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/DDS2/chr%s_noDup"%(i)
    outfilename="TDDlIST_B73_chr%s"%(i)
    checkTID(Folder,E,ddsFIle,outfilename)
    checkTID(Folder,TE_Middle, ddsFIle, outfilename)
    checkTID(Folder,TE_Terminal, ddsFIle, outfilename)



