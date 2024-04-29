from Rynolds import RynoldNumber


class NusseltNumber(object):

    def __init__(self,Gas:str,pressure:float=1*10**5,temp:float=100):
        self.rynolds=RynoldNumber(pressure=pressure,Gas=Gas,temp=temp)
        
    def forced_conv_plate(self,u_infinity:float,length):
        rynolds=self.rynolds.Calculate(u_infinity=u_infinity,length=length)
        if rynolds[0]<5*(10**5):
            Nu=0.664*(rynolds[0]**0.5)*(rynolds[1]**(1/3))
        elif rynolds[0]>5*(10**5):
            Nu=(0.037*(rynolds[0]**(4/5))-871.3)*(rynolds[1]**(1/3))
        return Nu
    
    def forced_constant_heat_flux_plate(self,u_infinity:float,length): 
    
        rynolds=self.rynolds.Calculate(u_infinity=u_infinity,length=length)
        Nu=0.680*(rynolds[0]**0.5)*(rynolds[1]**(1/3))
        return Nu
    
    def cylinder_in_cross_flow(self,u_infinity:float,diameter):
        rynolds=self.rynolds.Calculate(u_infinity=u_infinity,length=diameter)

        if 0.4<rynolds[0] & rynolds[0]<4: # Table 7.2 Page 458
            C=0.989
            M=0.330
        elif 4<=rynolds[0] & rynolds[0]<40:
            C=0.911
            M=0.385
        elif 40<=rynolds[0] & rynolds[0]<4000:
            C=0.683
            M=0.466
        elif 4000<=rynolds[0] & rynolds[0]<40000:
            C=0.193
            M=0.618
        elif 40000<=rynolds[0] & rynolds[0]<400000:
            C=0.027
            M=0.805
        Nu=C*(rynolds[0]**M)*(rynolds[1]**(1/3))
        return Nu
        