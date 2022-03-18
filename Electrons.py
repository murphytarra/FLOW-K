# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:14:40 2021

@author: murph
"""


import numpy as np

from numpy import linalg as LA
import matplotlib.pyplot as plt
from numpy.linalg import multi_dot
from numpy.linalg import inv
import math
import cmath

class Electrons:
    def __init__(self, dim, H, V, kT):
        self.dim = dim
        self.H = H
        self.V = V;
        self.kT = kT;
        
    #Tight Bonding Hamiltonian for a N level system 
    def TB_Hamil(self, N, eps, gamma):
        H = np.zeros((N, N));
        for i in range(0, N, 1):
            for j in range(0, N, 1):
                if i == j:
                    H[i][j] = eps;
                if i == j + 1:
                    H[i][j] = gamma;
                if j == i + 1:
                    H[i][j] = gamma;
        self.H = H;