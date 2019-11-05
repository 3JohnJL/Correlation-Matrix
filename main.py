# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 01:16:05 2016

@author: lydia jj
"""

xS={}
xDr={}
xSc={}
xDrc={}

data=open('maindata2.txt','r') 



for i in range(6):
    mydata=data.readline()
    s=mydata.split()

    point=s[0]
    S=float(s[1])
    Sc=float(s[2])
    Dr=float(s[8])
    Drc=float(s[9])
    
    xS[i+1]=S
    xDr[i+1]=Dr
    xSc[i+1]=Sc
    xDrc[1+1]=Drc

print(xSc[1])
    

import numpy
import sympy 
 
abS, abD = sympy.symbols('abS abD')
bcS, bcD = sympy.symbols('bcS bcD')
cdS, cdD = sympy.symbols('cdS cdD')
deS, deD = sympy.symbols('deS deD')
efS, efD = sympy.symbols('efS efD')
fgS, fgD = sympy.symbols('fgS fgD')


abSc, abDc = sympy.symbols('abSc abDc')
bcSc, bcDc = sympy.symbols('bcSc bcDc')
cdSc, cdDc = sympy.symbols('cdSc cdDc')
deSc, deDc = sympy.symbols('deSc deDc')
efSc, efDc = sympy.symbols('efSc efDc')
fgSc, fgDc = sympy.symbols('fgSc fgDc')
                         
ax, ay, bx, by, cx, cy, dx, dy, ex, ey, fx, fy, gx, gy = sympy.symbols('ax ay bx by cx cy dx dy ex ey fx fy gx gy')    

                     
bx = (abS*(sympy.cos(abD)))
by = (abS*(sympy.sin(abD))) 

cx = (bx + bcS*(sympy.cos(bcD)))
cy = (by + bcS*(sympy.sin(bcD)))

dx = (cx + cdS*(sympy.cos(cdD)))
dy = (cy + cdS*(sympy.sin(cdD)))

ex = (dx + deS*(sympy.cos(deD)))
ey = (dy + deS*(sympy.sin(deD)))

fx = (ex + efS*(sympy.cos(efD)))
fy = (ey + efS*(sympy.sin(efD)))

gx = (fx + fgS*(sympy.cos(fgD)))
gy = (fy + fgS*(sympy.sin(fgD)))

eqns = sympy.Matrix([bx,by,cx,cy,dx,dy,ex,ey,fx,fy,gx,gy])

J = eqns.jacobian([abS,abD,bcS,bcD,cdS,cdD,deS,deD,efS,efD,fgS,fgD])
F = J.subs({abSc: xSc[1] ,abDc:xDrc[1] , bcSc:xSc[2], bcDc:xDrc[2], cdSc:xSc[3] ,cdDc:xDrc[3] ,deSc:xSc[4] ,deDc:xDrc[4] ,efSc:xSc[5] ,efDc:xDrc[5] ,fgSc:xSc[6] ,fgDc:xDrc[6] })

Cv = numpy.diag(xSc[1] ,xDrc[1] , xSc[2], xDrc[2], xSc[3] ,xDrc[3] ,xSc[4] ,xDrc[4] ,xSc[5] ,xDrc[5] ,xSc[6],xDrc[6] )

Cav = F*Cv*(F.T)


correlation = sympy.eye(12)


for i in range(12):
    for j in range(12):
        if j > i:
            crr = Cav[i, j] / (sympy.sqrt(Cav[i,i]) * sympy.sqrt(Cav[j,j]))
            
            correlation[i,j] = crr
            correlation[j,i] = crr

printFile = numpy.asarray(correlation)

numpy.savetxt("Correlation Matrix.csv", printFile, delimiter=",")

       