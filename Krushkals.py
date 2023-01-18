#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:45:04 2023

@author: iot-b1
"""
#2
def Parent(s,pa):
    while(pa[s]):
        s=pa[s]
    return s ;
def kruskals(n,matrix):  
    prnt=[None for i in range (n)]
    i=1
    while(i<n):
        inf = 9999999
        for j in range (n):
            prnt[j]=0
            for k in range (n):
                if(matrix[j][k]!=0 and matrix[j][k]<inf):
                    inf=matrix[j][k]
                    a=c=j
                    b=d=k
        c=Parent(c,prnt)
        d=Parent(d,prnt)
        if(c!=d):
            prnt[c]=d
            print(b," ",a,"  ",inf)
            i+=1
        matrix[a][b]=0
num=6
mat=[[0,10,0,0,0,8],
     [0,0,1,2,0,0],
     [0,0,0,0,0,0],
     [0,0,-2,0,0,0],
     [0,-4,0,-1,0,0],
     [0,0,0,0,1,0]]
print()
kruskals(num,mat)