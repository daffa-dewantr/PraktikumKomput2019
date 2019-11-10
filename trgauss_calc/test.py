# -*- coding: utf-8 -*-

import InterpolatePol as ip
import numpy as np

x = np.array([0.0,1.0,2.5,3.0,4.0])
y = np.array([1,0.5,-0.4161,-1.9900,-2.6536])
n_polinom = 5

ip.plot_intp(x,y)