import numpy as np
import InterpolatePol as ip

x = np.array([0.0,1.0,2.5,3.0,4.0])
y = np.array([1,0.5,-0.4161,-0.9900,-0.6536])
n_polinom = 5

x = ip.plot_intp(x, y)