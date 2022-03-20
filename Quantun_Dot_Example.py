2# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 09:25:31 2021

@author: murph

Here we investigate how an external periodic electric field 
effects the overall charge transport through a Double Quantum Dot device

"""

import numpy as np

from numpy import linalg as LA
import matplotlib.pyplot as plt
from numpy.linalg import multi_dot
from numpy.linalg import inv
import math
import cmath

from Electrons import Electrons
from E_field import E_field
from coupling2 import coupling2
from coupling3 import coupling3
from calc_trans import calc_trans


##Initially we write the Hamiltonian of our QD system
hh = [[-5, 1], [1, 5]]

##Next we set our external parameters
T = 0.01 #temperaure
V = 0.0 #applied bias
Gamma = (0.5) #Coupling to electron resoirvoirs/leads

n = 2 #Dimensions of thesystem

Coupling =[10] #Coupling between electric field and central system
m_max = 5 #number of Green Functions calculated
m = 800 #number of steps when calculating current for one electric field
E_to_scan = np.linspace(0, 14, 100)#np.linspace(0, 14, 100) #range of electric field frequencies to scan
V_to_scan = 0#np.linspace(-12, -7.5, 100)
    
#CURRENT FOR DIFFERENT ELECTRIC FIELD FREQUENCIES 
results = []   
 
plt.figure()     
for i in Coupling:
    #Scan through range of different couplings if desired
    
    print(i)
    Hamiltonian = Electrons(n, hh, V_to_scan,T);   #define hamiltonain
    E = E_field( -14, 0.1, E_to_scan, Gamma, i/2, i/2) #define electric field
    current = coupling2(E, Hamiltonian, m,m_max) #calculate curren (see coupling2 function)
    results.append(current)

    #Plot results
    plt.plot(E_to_scan[0:], (current[0:]), linestyle="-", linewidth=1, marker = "o", markersize = 0)#, label = "V = " + str(i) + " [t]")
    plt.ylabel("Normalised Current")
    plt.xlabel(" Applied Bias accross Leads [t]")
    #plt.yscale('log')
    #plt.title("V = " + str(V))
    plt.grid("on")
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.style.use('ggplot')

plt.show()

