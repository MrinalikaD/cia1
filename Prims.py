# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#1
def Prims(n,matrix):
    prnt = []
    vst=[]
    wt=[]
    for i in range(n):
        wt.append(9999999)
        vst.append(0)
        prnt.append(-1)
    wt[0]=0
    for i in range (n):
        inf=9999999
        for j in range (n):
            if(vst[j]==0 and wt[j]<inf):
                inf=wt[j]
                ver=j
        vst[ver]=1
        for j in range (n):
            if (matrix[ver][j]!=0 and matrix[ver][j]<wt[j]):
                prnt[j]=ver
                wt[j]=matrix[ver][j]    
    for i in range (1,n):
        print(i," ",prnt[i],"  ",wt[i])   
num=6
mat=[[0,10,0,0,0,8],
     [0,0,1,2,0,0],
     [0,0,0,0,0,0],
     [0,0,-2,0,0,0],
     [0,-4,0,-1,0,0],
     [0,0,0,0,1,0]]
Prims(num,mat)
