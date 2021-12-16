"""
This file consist main plotter code for DryVR reachtube output
"""

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np 
from typing import List 

colors = ['red', 'green', 'blue', 'yellow', 'black']

def plot(data, x_dim: int = 0, y_dim_list: List[int] = [1], color = 'b', fig = None):
    if fig is None:
        fig = plt.figure()
    ax = plt.gca()
    x_min = float('inf')
    x_max = -float('inf')
    y_min = float('inf')
    y_max = -float('inf')
    for rect in data:
        lb = rect[0]
        ub = rect[1]
        for y_dim in y_dim_list:
            rect_patch = patches.Rectangle((lb[x_dim], lb[y_dim]), ub[x_dim]-lb[x_dim], ub[y_dim]-lb[y_dim], color = 'b')
            ax.add_patch(rect_patch)
            x_min = min(lb[x_dim], x_min)
            y_min = min(lb[y_dim], y_min)
            x_max = max(ub[x_dim], x_max)
            y_max = max(ub[y_dim], y_max)

    ax.set_xlim([x_min-1, x_max+1])
    ax.set_ylim([y_min-1, y_max+1])
    return fig
