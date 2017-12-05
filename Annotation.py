
import os



def Annotation(Gff,TIDList,output,Folder):
    os.chdir(Folder)
    f=open(output,'a')
    GffFile=open(Gff,'r+')
    TIDfile=open(TIDList,'r+')
    TIDlines=TIDfile.readlines()
    Gfflines=GffFile.readlines()
    for line in TIDlines:
        Column_T=line.split()
        for line1 in Gfflines:
            Column_G=line1.split()
            if(Column_G[0]=="#"):
                continue
            if((int(Column_G[3])<int(Column_T[1]) and int(Column_G[4])>int(Column_T[2]) and Column_G[3]!='1') or (int(Column_G[3])>int(Column_T[1]) and int(Column_G[4])<int(Column_T[2]))):
                f.write(str(Column_T[1])+" "+ line1)
    f.close()


def Annotation1(Gff,TIDList,output,Folder):
    os.chdir(Folder)
    f=open(output,'a')
    GffFile=open(Gff,'r+')
    TIDfile=open(TIDList,'r+')
    TIDlines=TIDfile.readlines()
    Gfflines=GffFile.readlines()
    for line in TIDlines:
        Column_T=line.split()
        for line1 in Gfflines:
            Column_G=line1.split()
            if(Column_G[0]=="#"):
                continue
            if((int(Column_G[3])<int(Column_T[1]) and int(Column_G[4])>int(Column_T[2]) and Column_G[3]!='1') or (int(Column_G[3])>int(Column_T[1]) and int(Column_G[4])<int(Column_T[2]))):
                f.write(str(Column_T[1])+" "+ line1)
    f.close()

# for i in range(1,11):
#     Annotation("/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/Annotation/B73_Gff_Chr%s"%(i),
#                "/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/1009/TID_Target/Maize_chr%s_Target" % (i),
#                "DupGene_%s"%(i), "/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/1009/"
#                )


def SplitGff(Folder,Gff,Length,OutputName):
    os.chdir(Folder)
    ID=' '
    f=open(OutputName,'a')
    GffFile = open(Gff, 'r+')
    lines=GffFile.readlines()
    for line in lines:
        column=line.split()
        if(column[0][0]=="#"):
            continue
        if(column[2]=="region" and column[4]==str(Length)):
            ID=column[0]
            break
    for line1 in lines:
        column1 = line1.split()
        if(column1[0]==ID):
            f.write(line1)
    f.close()

# Length=[307041717,244442276,235667834,246994605,223902240,174033170,182381542,181122637,159769782,150982314]
# for i in range(1,11):
#     length=Length[i-1]
#     OutputName="B73_Gff_Chr%s"%(i)
#     SplitGff("/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/Annotation/","/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/Annotation/GCA_000005005.6_B73_RefGen_v4_genomic.gff", length, OutputName)
#

def SplitTEGff(Folder,TE_Annotation, DDSfile, OutputName,Chr):
    os.chdir(Folder)
    out=open(OutputName,'a')
    TE_gff=open(TE_Annotation,'r+')
    DDS_file=open(DDSfile,'r+')
    TElines=TE_gff.readlines()
    DDS_lines=DDS_file.readlines()
    for TEline in TElines:
        TE_column=TEline.split()
        if(TE_column[0]==str(Chr)):
            for DDS_line in DDS_lines:
                if((int(DDS_line.split()[1])<int(TE_column[3]) and int(DDS_line.split()[2])>int(TE_column[4]))
                   or (int(DDS_line.split()[1])>int(TE_column[3]) and int(DDS_line.split()[2])<int(TE_column[4]))):
                    out.write(DDS_line.split()[1]+" "+TEline)
    out.close()
    TE_gff.close()
    DDS_file.close()


# SplitTEGff("/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/",
#            "/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/Annotation/B73v4.TE.filtered.gff3",
#            "/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/DDS2/chr1_noDup",
#            "Chr1_TE_Repeats",1)

def ContTE_Repeats(File):
    f=open(File,'r+')
    list=[]
    lines=f.readlines()
    for line in lines:
        column=line.split()
        list.append(column[0])
    print(len(list))
    s=set(list)
    print(len(s))



def ClearBlastResult(BlastOut, Output,Folder):
    os.chdir(Folder)
    BlastFile=open(BlastOut,'r+')
    Blastlines=BlastFile.readlines()
    Outfile=open(Output,"a+")
    for line in Blastlines:
        columns=line.split()
        if(columns[0]=="#" or int(columns[13])<80):
            continue
        newline=columns[0]+" "+ columns[1]+" "+columns[3]+" "+columns[4]+" "+columns[7]+" "+ columns[8]+" "+columns[9]+" "+columns[10]+" "+columns[13]+ "\n"

        Outfile.write(newline)
    BlastFile.close()
    Outfile.close()

ClearBlastResult("AllTEblastGenome","AllTEout","/Users/weijiasu/Dropbox/Research/BioinformaticsProject/Maize_B73/")