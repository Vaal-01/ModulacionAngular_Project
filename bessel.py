import math
from math import factorial
import numpy as np
import scipy
import scipy.special
from scipy.special import jve

def getJn(m,vc):
    vc = float(vc)
    m = float(m)
    toReturn = np.array([])
    n = 0
    while True:
        newJ = float("{:.2f}".format(jve(n, m)))
        
        if (abs(newJ) < 0.01):
          break
        toReturn = np.append(toReturn, newJ*vc)
        n+=1
    return toReturn

def getn(m):
    m = float(m)
    n = 0
    while True:
        newJ = float("{:.2f}".format(jve(n, m)))
        if (abs(newJ) < 0.01):
          break
        n+=1
    return n

def getlateral(m):
    m = float(m)
    toReturn = np.array([])
    n = 0
    while True:
        newJ = float("{:.2f}".format(jve(n, m)))
        
        if (abs(newJ) < 0.01):
          break
        toReturn = np.append(toReturn, newJ)
        n+=1
    return toReturn


class Bessel:

    def Pt(J, RL):
      toReturn = -J[0]**2
      toReturn+=2*sum((J**2))
      return toReturn/(2*RL)

    def Pbl(m, Pc):
      return math.pow(m, 2)*Pc/4

