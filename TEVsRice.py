
import os
import subprocess

import sys
import os
import subprocess

import subprocess
import glob

from Bio import SeqIO


from Bio.Blast.Applications import NcbiblastnCommandline
from io import StringIO
from Bio.Blast import NCBIXML
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Blast import NCBIXML
import subprocess
import glob

import sys


def distance(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2


def numberOfBoomerangs(points):
    n=0
    if (len(points) < 3):
        return 0
    list1 = []
    for i in range(0, len(points)):
        for j in range(i + 1, len(points)):
            dis = distance(points[i], points[j])
            list1.append(dis)
    set1 = set(list1)
    for e in set1:
        if (list1.count(e) > 1):
            n = n + list1.count(e)
    return n

print(numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))