import numpy as np
import matplotlib.pyplot as plt

def do_the_plot(dest):
    x = np.r_[0:np.pi:100j]
    y = np.sin(x)
    plt.plot(x, y)
    plt.savefig("app" + dest, format='png')
    
