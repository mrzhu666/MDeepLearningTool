# import os

# os.system("conda list")

from math import *

U=15.25
P=3.2
I=0.3
R=10
w=2*3.14*50
                  
Z=U/I
r=P/I**2-R
X=sqrt(Z**2-r**2)
L=X/w
Sz=U*I
Pz=P-I**2*R
Qz=sqrt(Sz**2-Pz**2)
phi=acos(Pz/Sz)

print(Z,r,L,phi)

print(Sz,Qz)