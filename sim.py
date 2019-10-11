import numpy as np
import pdb
import matplotlib.pyplot as plt

def g1(i, inv = False):
    if(inv):
        if(i==1):
            return {1}
        elif(i==2):
            return {2}
        elif(i==3):
            return {3}
        elif(i == 4):
            return {4}
        elif(i == 6):
            return {5}
        else:
            return 0
    if(i==1):
        return 1
    elif(i==2):
        return 2
    elif(i==3):
        return 3
    elif(i == 4):
        return 4
    elif(i == 5):
        return 6
    else:
        return 0
def g2(i, inv = False):
    if(inv):
        if(i==2):
            return {1, 3}
        elif(i == 4):
            return {2, 4, 5}
        else: return 0
    if(i==1 or i==3):
        return 2
    elif(i == 2 or i == 4 or i == 5):
        return 4
    else: return 0
def g3(i, inv = False):
    if(inv):
        if(i==3):
            return {1}
        elif(i==5):
            return {2, 3}
        elif(i==1):
            return {4}
        elif(i==2):
            return {5}
        else:
            return 0
    if(i==1):
        return 3
    elif(i==2):
        return 5
    elif(i==3):
        return 5
    elif(i==4):
        return 1
    elif(i==5):
        return 2
    else:
        return 0

def rv(p1 = 0.25, p2 = 0.17, p3 = 0.25, p4 = 0.17, p5 = 0.16):
    tmp = np.random.random()
    if(tmp < p1):
        return 1
    elif(tmp >= p1 and tmp < p1+p2):
        return 2
    elif(tmp >= p1+p2 and tmp < p1+p2+p3):
        return 3
    elif(tmp >= p1+p2+p3 and tmp < p1+p2+p3+p4):
        return 4
    elif(tmp >= p1+p2+p3+p4 and tmp < p1+p2+p3+p4+p5):
        return 5

nk = np.array([0,0,0])
Ik = np.array([1000, 1000, 1000])
uk = np.array([0,0,0])
phi_hat = np.array([[0,0,0],[0,0,0],[0,0,0]])
B = 7
arm = []
regret = [0]


for i in range(10):
    kmax = nk.argmax()
    A = set([0,1,2])
    for k in set(set(A)-set({kmax})):
        if(uk[kmax] > phi_hat[k, kmax]):
            A =  A - set({k})

    kt = np.argmax(Ik)
    x_ = rv()
    print(kt, x_)
    if(kt == 0):
        reward = g1(x_)
    elif(kt == 1):
        reward = g2(x_)
    elif(kt == 2):
        reward = g3(x_)
    nk[kt]+=1
    uk[kt] = (uk[kt]*(nk[kt]-1)+reward)/nk[kt]
    Ik[kt] = uk[kt] + B*np.sqrt(2*np.log(i+1)/nk[kt])
    if(kt == 0):
        x = g1(reward, True)
        max2 = 0
        max3 = 0
        for x in x:
            r_tmp_2 = g2(x)
            r_tmp_3 = g3(x)
            if(r_tmp_2 > max2):
                max2 = r_tmp_2
            if(r_tmp_3 > max3):
                max3 = r_tmp_3
            phi_hat[1, 0] = (phi_hat[1, 0]*(nk[kt]-1) + max2)/nk[kt]
            phi_hat[2, 0] =  (phi_hat[2, 0]*(nk[kt]-1) + max3)/nk[kt]

    elif(kt == 1):
        x = g2(reward, True)
        max1 = 0
        max3 = 0
        for x in x:
            r_tmp_1 = g1(x)
            r_tmp_3 = g3(x)
            if(r_tmp_1 > max1):
                max1 = r_tmp_1
            if(r_tmp_3 > max3):
                max3 = r_tmp_3
            phi_hat[0, 1] = (phi_hat[0, 1]*(nk[kt]-1) + max1)/nk[kt]
            phi_hat[2, 1] =  (phi_hat[2, 1]*(nk[kt]-1) + max3)/nk[kt]


    elif(kt == 2):
        x = g3(reward, True)
        max1 = 0
        max2 = 0
        for x in x:
            r_tmp_1 = g1(x)
            r_tmp_2 = g2(x)
            if(r_tmp_1 > max1):
                max1 = r_tmp_1
            if(r_tmp_2 > max2):
                max2 = r_tmp_2
            phi_hat[0, 2] = (phi_hat[0, 2]*(nk[kt]-1) + max1)/nk[kt]
            phi_hat[1, 2] =  (phi_hat[1, 2]*(nk[kt]-1) + max2)/nk[kt]

    arm.append(kt)
    regret.append(regret[-1]+g3(x_) - reward)

plt.plot(regret)
plt.show()
#plt.plot(arm)
#plt.show()
