# Interpolation is important method to use
# with experimental data.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

#Entering X and Y values
class Interp(object):
    def __init__(self,Xaxis:list[float],Yaxis:list[float]):
        self.x =np.array(Xaxis, float)
        self.y = np.array(Yaxis, float) 
        self.n = len(self.x)
        self.p = np.zeros([self.n, self.n+1])


    def newton_interpol(self,z):
      f_list = []
      for m in z:
       
        for i in range(self.n):
          self.p[i, 0] = self.x[i]
          self.p[i, 1] = self.y[i]
    
        for i in range(2, self.n+1): 
          for j in range(self.n+1-i):
            self.p[j,i] = ( self.p[j+1, i-1] - self.p[j, i-1] ) / ( self.x[j+i-1] - self.x[j] )
            
        np.set_printoptions(suppress=True)
    
        #Coefficients
        b = self.p[0][1:]  
    
        lst = [] 
    
        t = 1
        for i in range(len(self.x)):
          t *= (m-self.x[i]) 
          lst.append(t)
    
        f = b[0]
        for k in range(1,len(b)):
          f += b[k] * lst[k-1] 
        f_list.append(f)
      return f_list
if __name__ == "__main__":
    inter=Interp([0, 2, 4, 6, 8, 10],[0, 1.5, 2, 2.5, 3, 3])
    z = [3.1111]
    print("The value of polynomial: ", inter.newton_interpol(z))