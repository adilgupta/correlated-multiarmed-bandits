import numpy as np

def g1(i):
    if(i==1):
        return 1;
    else if(i==1):
        return 2;
    else if(i==3):
        return 3;
    else if(i == 4):
        return 4;
    else if(i == 5):
        return 6;
    else:
        return 0;
def g2(i):
    if(i==1 or i==3):
        return 2;
    else if(i == 2 or i == 4 or i == 5):
        return 4;
    else return 0;
def g3(i):
    if(i==1):
        return 3;
    else if(i==2):
        return 5;
    else if(i==3):
        return 5;
    else if(i==4):
        return 1;
    else if(i==5):
        return 2;
    else:
        return 0;

nk = np.array([0,0,0])
Ik = np.array([1000, 1000, 1000])
uk = np.array([0,0,0])

for i in range(100):
    kmax = nk.argmax()
    A = set([0,1,2])
    for k in A-set(kmax):
