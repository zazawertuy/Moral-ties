# -*- coding: utf-8 -*-
"""
Created on Feb 18 17:35:17 2021

@author: jmarco
"""
from sys import argv
import numpy as np
import math
import time
import random
import csv
###############################################################################
# Read the file. 
start = time.time()
with open("\\Users\\xxxx\\Desktop\\Moral Ties\\net_1000\\100.txt") as f:
    f=[x.strip() for x in f if x.strip()]
    data=[tuple(map(int,x.split())) for x in f[0:]]
    IN=[x[0] for x in data]
    OUT=[x[1] for x in data]
    #print('IN',IN)
    #print('OUT',OUT)
    print (len(IN))
###############################################################################
###############################################################################
#                            - FUNCTIONS -                                    #
###############################################################################
###############################################################################
#1. Neighbors
#------------------------------------------------------------------------------
def neighbors(node):
    areIN=[i for i,x in enumerate(IN) if x == node]
    areOUT=[i for i,x in enumerate(OUT) if x == node]
    neighbors = []
    for i in areIN:
        neighbors.append(OUT[i])
    for i in areOUT:
        neighbors.append(IN[i])
    
    return [sorted(neighbors)]
###############################################################################
#2. Uniform 
#------------------------------------------------------------------------------
def runif(Edges,p):
    s=[]
    a=np.random.uniform(0,1,(Edges,))
    for i in range(len(a)):
        if a[i] >= p:
            s.append(1)
        else:
            s.append(0)
    #sum(runif(30,0.5)[0])
    return [s]
###############################################################################
#3. Strategy 
#------------------------------------------------------------------------------
def strategy(node,population):
    a=population[node]
    return [a]
#------------------------------------------------------------------------------
def A_strategy(node,a,population):
    pol=a[0][node][0]
    strt=[ strategy(x, population)[0] for x in pol]
    return [strt]
#A_strategy(a[0][1000][0])[0][0][0]
#A_strategy(1000,a,population)[0]
###############################################################################
#4. Nodes 
#------------------------------------------------------------------------------
def nodes():
    q=len(set(IN+OUT))
    return [q]
#int(nodes()[0])
###############################################################################
#5. Neighborhood
#------------------------------------------------------------------------------
def neighborhood():
    neighd=[]
    for i in range(int(nodes()[0])):
        neighd.append(neighbors(i))
    return [neighd]
    
###############################################################################
#6. Clustering Coefficient
#------------------------------------------------------------------------------
def groupSize(node,a):
    links = 0
    for w in  a[0][node][0]:
        for u in  a[0][node][0]:
            if u in  a[0][w][0]: links += 0.5
    return (2.0*links)/(len(neighbors(node)[0])*(len(neighbors(node)[0])-1))
#------------------------------------------------------------------------------
def local_T():
    t=[]
    for i in range(int(nodes()[0])):
        t.append(groupSize(i,a))
    return [t]
#------------------------------------------------------------------------------
def indirectMoralTies(node,a,population):
    ss=A_strategy(node,a,population)[0]
    sst=[i for i in range(len(ss)) if ss[i] != 0]
    links = 0
    for w in  sst:
        for u in  sst:
            if a[0][node][0][u] in a[0][a[0][node][0][w]][0]: links += 0.5
    return (2.0*links)/(len(neighbors(node)[0])*(len(neighbors(node)[0])-1))
###############################################################################
###############################################################################
#                            - INITIAL CONDITIONS -                           #
###############################################################################
###############################################################################
n=nodes()[0]
time_period=1
cooperantes = []
nivel = []
p=0.5
population=runif(nodes()[0],1-p)# 1 - p denotes the share of compliers
population=population[0]
cooperantes.append(sum(population))
a=neighborhood()
###############################################################################
###############################################################################
#                            - ANALYSIS -                                     #
###############################################################################
###############################################################################
sc=float(sum(population))/n
for j in range(time_period):
    for i in range(n): 
        cc=indirectMoralTies(i,a,population) # INDIRECT MORAL TIES
        ct=groupSize(i,a)
        sp=A_strategy(i,a,population)[0]
        fc=(float(sum(sp))/len(sp))*100  # DIRECT MORAL TIES
        if fc > 99:
            fc=99
        with open('\\Users\\xxxx\\Desktop\\Moral Ties\\fc.txt','a') as fR:
            fR.write('%.5f\n' % fc)
            fR.close()
        with open('\\Users\\xxxx\\Desktop\\Moral Ties\\cc.txt','a') as fR:
            fR.write('%.5f\n' % cc)
            fR.close()
        with open('\\Users\\xxxx\\Desktop\\Moral Ties\\ct.txt','a') as fR:
            fR.write('%.5f\n' % ct)
            fR.close()
    print(j)
end = time.time()
print(end - start)
