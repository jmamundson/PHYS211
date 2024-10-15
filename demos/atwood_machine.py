#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:56:27 2024

@author: jason
"""

import numpy as np


g = 9.81 # gravity [m s^-2]
I = 1.8e-6 # moment of inertia of the pulley [kg m^2]
r = 0.051/2 # radius of the pulley [m]
mp = 0.005 # mass of the pulley [kg]

# if pulley was a disk
I_disk = 0.5*mp*r**2 # momentum of inertia of disk [kg m^2]


m2 = 0.255 # mass 2 [kg]
m1 = 0.250 # mass 1 [kg]

dy = 0.175 # distance that mass falls [m]
dt = 2.3 # time to hit the ground [s]

a = 2*dy/dt**2 # observed acceleration [m s^-12]
alpha = -a*r


a_massless = (m2-m1)/(m1+m2)*g # acceleration if mass and friction ignored
a_frictionless = (m2-m1)/(m1+m2+I/r**2)*g # acceleration if friction neglected

dt_massless = np.sqrt(2*dy/a_massless)
dt_frictionless = np.sqrt(2*dy/a_frictionless)



T1 = m1*(g+a)
T2 = m2*(g-a)

tauF = I*alpha + r*(T2-T1)

tauT1 = r*T1
tauT2 = r*T2