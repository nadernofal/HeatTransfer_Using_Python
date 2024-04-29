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
    
    