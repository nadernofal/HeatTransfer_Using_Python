#book: incropera Appendix A.4
import json

with open("./Properties_table.json",encoding="UTF-8",mode="r") as file:
    properties=json.load(file)


import pandas as pd
from interpolation import Interp
class RynoldNumber(object):
    def __init__(self,Gas:str,pressure:float=1*10**5,temp:float=100):
        """
        Gas is a string: air, o2, n2, h2, nh3, co2 and co
        Temperature in kelvin
        Pressure in Pascal N/m^2
        """
        if pressure!=1*10**5:
            pressure_considered=True
        self.pd=pd.DataFrame(properties[Gas])
        self.Value=0
 
        

        # getting the viscosity by newton interpolation
        Viscosity=Interp(Xaxis=self.pd['temp'].to_list(),Yaxis=self.pd['kyn_vis'].to_list())
        self.Vis=Viscosity.newton_interpol(temp)[0]

        if pressure_considered:
                
            # getting the viscosity by newton interpolation
            dynb_Viscosity=Interp(Xaxis=self.pd['temp'].to_list(),Yaxis=self.pd['vis'].to_list())
            vis=dynb_Viscosity.newton_interpol(temp)[0]

            density1=Interp(Xaxis=self.pd['temp'].to_list(),Yaxis=self.pd['Density'].to_list())
            d1=density1.newton_interpol(temp)[0]
            p1=1*10**5
            p2=pressure
            d2=(p2/p1)*d1 #PV=MRT
            self.Vis=vis/d2 
    
    def Calculate(self,u_infinity:float,length):
        """
        U infinity is the velocity of the fluid in m/s
        length: if flat plate then its the actual length of the plate parallel to the streamline of the flow, if a pipe then it is the diameter
        """
        self.Value = (u_infinity*length)/self.Vis
        return self.Value
    