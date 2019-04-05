import numpy as np
import matplotlib.pyplot as plt
import os.path as osp
import sys

def check_fun(fun_name):
    available_funs ={
        'sin': np.sin,
        'cos': np.cos,
        'exp': np.exp,
        'log': np.log
    }
    return available_funs.get(fun_name, None)


def do_the_plot(dest, x0, xk, fun):
    x0 = float(x0)
    xk = float(xk)
    x = np.r_[x0:xk:101j]
    y = fun(x)

    plt.cla()
    plt.plot(x, y)
    file_name = osp.join(dest, str(np.random.randint(1000)) +".png")
    path = "app" + file_name
    plt.savefig(path, format='png')
    return file_name

    
