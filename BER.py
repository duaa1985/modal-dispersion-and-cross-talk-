import fiber
import numpy
import fiber
import numpy
import pickle
import math, sys
import scipy
from math import factorial,log10
from numpy import linalg as LA
from scipy.linalg import expm
from scipy.linalg import norm
length=300
step_length=1
n_sections=int(length / step_length)
sigma_kappa =  10.0
sigma_theta = 0.36
diameter = 25e-6
W = 1.55e-6
c=3e8
Eb_N0 = numpy.arange(0, 30, .5)
Kappa_list = numpy.random.randn(n_sections)
theta_list = numpy.random.randn(n_sections)
test_fiber=fiber.LargeCoreMMF(length=length,step_length=step_length,a=diameter)
M=len(test_fiber.admissible_modes)
kappa_vals = numpy.abs(sigma_kappa*Kappa_list)
theta_vals = sigma_theta*theta_list
t = numpy.arange(0, 1.01e10, 1e8)
U01,U01_d = test_fiber.calculate_matrix(L=W, kappa_vals=kappa_vals, theta_vals=theta_vals, splice_every = 60)
U01=numpy.mat(U01)
U01_d = numpy.mat(U01_d)
F1 = 1.0j*numpy.dot(U01.H,U01_d)
F1 = 0.5 * (F1 + F1.H)
G1,P1= LA.eig(F1)
Q1 = numpy.dot(U01,P1[:,0])
   
def calculate_mag_resp(Omega, U, P1, Q1):
    return numpy.abs(numpy.dot(Q1.H,numpy.dot(U, P1[:,0])))
l=0
for Omega in t:
    U_F_imp = 2*calculate_mag_resp(Omega,U01 * expm(-1.0j * Omega * F1), P1, Q1)
    U11,U11_d = test_fiber.calculate_matrix(L=c/(c/W+Omega), kappa_vals=kappa_vals, theta_vals=theta_vals, splice_every = 60)
    U11 = numpy.mat(U11)
    U_T_imp = 2*calculate_mag_resp(Omega, U11, P1, Q1)
    E=[]
    R=[]
    l += 1
    print l
    for j in range(len(Eb_N0)):
        g=pow(10,(Eb_N0[j]/20.0))
        BER_F=.5*scipy.special.erfc(math.sqrt(pow(U_F_imp[0,0],2)*g))
        BER_T=.5*scipy.special.erfc(math.sqrt(pow(U_T_imp[0,0],2)*g))
        E.append(BER_F)
        R.append(BER_T)
    filename1='lossy_BER_2_First_response multi mode_offset2 300m'+str(l)
    filename2 = 'lossy_BER_2_Higher_response multi mode_offset2 300m'+str(l)
    f1=open(filename1,'w')
    f2 = open(filename2,'w')
    pickle.dump(E,f1)
    pickle.dump(R,f2)
    f1.close()
    f2.close()            
 
sys.exit(0)


