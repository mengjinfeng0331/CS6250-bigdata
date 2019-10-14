# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 22:45:03 2019

@author: victor
"""

import numpy as np

from bokeh.plotting import figure, output_file, show

N=300

x=np.random.randint(0,100,size=(N))
y=np.random.randint(0,100,size=(N))
r=np.random.randint(0,4,size=N)
color=['#{:2x}{:2x}{:2x}'.format(i,j,30) for i,j in zip(50+2*x, 50+2*y)]

       
       
p=figure(title='circles',x_range=(0,100),y_range=(0,100))


p.circle(x,y,radius=r,fill_color=color,fill_alpha=0.5,line_color=None)

show(p)
