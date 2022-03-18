# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:11:50 2021

@author: murph
"""

import numpy as np

from numpy import linalg as LA
import matplotlib.pyplot as plt
from numpy.linalg import multi_dot
from numpy.linalg import inv
import math
import cmath

class E_field:
    def __init__(self, w_min, w_max, E_to_scan, SELF, Up, Um):
        self.w_min = w_min;
        self.w_max = w_max;
        self.E_to_scan = E_to_scan;
        self.Up = Up; self.Um = Um;
        self.SELF = SELF;
