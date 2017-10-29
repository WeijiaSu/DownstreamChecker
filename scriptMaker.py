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
