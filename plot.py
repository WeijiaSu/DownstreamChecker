import numpy as np
import matplotlib.pyplot as plt
import xlrd
import pandas as pd



# myBook = xlrd.open_workbook(r'/Users/weijiasu/Dropbox/Maize_B73_TDD_List.xlsx')
# mySheet = myBook.sheet_by_index(0)
# YList=[]
# XList=[]
# for i in range(0,10):
#     values=mySheet.col_values(i)
#     YList.append(values[1:])
#     XList.append(values[0])
#
# print(YList)
# print(XList)
# print(len(YList))
# print(len(XList))
#
# # chr1=XList[0][1]
# Y1=YList[0]
# X1=[1]*len(YList[0])
# X2=[2]*len(YList[1])
# print(YList[1])
# print(X2)
# print(X1)
# axes = plt.subplot(111)
# type1 = axes.scatter(X1, YList[0], marker = '_', s=20, c='red')
# # type2 = axes.scatter(X2, YList[1], marker = '_', s=40, c='green')
# plt.show()
X=np.arange(4)
total_width, n = 0.8, 4
width = 0.15
# X = X - (total_width - width) / 4

B54_M=[9,0,12,11]
B54_UM=[17,12,22,51]
M_257=[9,1,0,10]
UM_257=[17,11,24,52]
E3_M=[9,0,12,11]
E3_UM=[17,12,22,51]
S7_M=[8,0,3,11]
S7_UM=[18,12,21,51]
M_6D=[14,1,7,22]
UM_6D=[12,11,17,40]


fig, ax = plt.subplots()
plt.rcParams["patch.force_edgecolor"] = True
ax.bar(X, B54_UM, width, color='r',label='UnMethylated')
ax.bar(X, B54_M, width, bottom=B54_UM,color='yellow',label='Methylated')
# ax.set_xticks(X + width / 4)
# ax.set_xticklabels(("B54","B54","B54","B54"))
ax.bar(X+width, UM_257, width, color='r')
ax.bar(X+width, M_257, width, bottom=UM_257,color='yellow')
# Labels=["257","257","257","257"]
# ax.set_xticks(list(ax.get_xticks())+Labels)
# ax.set_xticklabels(("B54","B54","B54","B54"))
ax.bar(X+2*width, E3_UM, width, color='r')
ax.bar(X+2*width, E3_M, width, bottom=E3_UM,color='yellow')
ax.bar(X+3*width, S7_UM, width, color='r')
ax.bar(X+3*width, S7_M, width, bottom=S7_UM,color='yellow')
ax.bar(X+4*width, UM_6D, width, color='r')
ax.bar(X+4*width, M_6D, width, bottom=UM_6D,color='yellow')
ax.legend(loc="upper left",bbox_to_anchor=(0,1))
# ax.axis(X + width / 4)
# ax.axis(['G1', 'G2', 'G3', 'G4'])
# ax.set_xticks(X+2*width+ width / 100)

rects = ax.patches
for i in range(0,len(rects)):
    print(rects[i].get_x())
    print(rects[i].get_height())
labels = ["B54","257","E3","S7","6D"]*4
pos=[0,0.15,0.3,0.45,1,1.15,1.3,1.45,1.6 ,2,2.15,2.3,2.45,2.6,3,3.15,3.3,3.45,3.6]
# for rec in rects:
#     pos.append(rec.get_x() + rec.get_width() / 2)
print(pos)

# ax.set_xticks(pos,minor=True)
# ax.set_xticklabels(labels,minor=True, )
# ax.tick_params(axis='x', which='major', pad=15, size=0)
# plt.setp(ax.get_xticklabels(), rotation=0)

# for i in range(len(pos)):

# for i in range(0,len(labels)):
#     height = rects[i].get_height()
#     ax.text(pos[i], height + 5, labels[i], ha='center', va='bottom')


plt.show()