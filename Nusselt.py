from Rynolds import RynoldNumber

def Grashof_number(Temp_infinity:float,Temp_surface:float,Surface_Area,Volume,Vis)->float:
    """
    Grashof for a free convection case
    Temperatre in kelvine
    """
    Lc=Volume/Surface_Area
    b=2/(Temp_infinity+Temp_surface)
    Gr=9.81*b*(Temp_surface-Temp_infinity)*(Lc**3)/Vis
    return Gr


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
    
    def free_convection_vertical_plate(self,Temp_infinity:float,Temp_surface:float,Surface_Area,Volume):
        vis=self.rynolds.Vis
        Gr=Grashof_number(Temp_infinity,Temp_surface,Surface_Area,Volume,vis)
        Rayleigh=Gr*self.rynolds.Pr
        
        if Rayleigh<10**9:
            Nu=  0.68 + (0.670*(Rayleigh**0.25)/((1 + ((0.492/self.rynolds.Pr)**9/16))**4/9)) # Slightly better accuracy for laminar flow

        elif Rayleigh>10**9:
            Nu = (0.825 + (0.387*(Rayleigh**(1/6))/((1 + ((0.492/self.rynolds.Pr)**9/16))**(8/27))))**2

        return Nu
    
        
    def free_convection_horizantal_and_inclined_plate_hottop(self,Temp_infinity:float,Temp_surface:float,Surface_Area,Volume): 
        """
        Upper Surface of Hot Plate or Lower Surface of Cold Plate
        """
        vis=self.rynolds.Vis
        Gr=Grashof_number(Temp_infinity,Temp_surface,Surface_Area,Volume,vis)
        Rayleigh=Gr*self.rynolds.Pr

        if Rayleigh<=10**7 and Rayleigh >= 10**4:
            Nu=0.5 * Rayleigh**0.25 # Equation 9.30
        elif Rayleigh<=10**11 and Rayleigh >= 10**7:
            Nu=0.15 * Rayleigh**(1/3) # Equation 9.31
        return Nu

    def free_convection_horizantal_and_inclined_plate_coldtop(self,Temp_infinity:float,Temp_surface:float,Surface_Area,Volume): 
        """
        Lower Surface of Hot Plate or Upper Surface of Cold Plate
        """
        vis=self.rynolds.Vis
        Gr=Grashof_number(Temp_infinity,Temp_surface,Surface_Area,Volume,vis)
        Rayleigh=Gr*self.rynolds.Pr

        Nu=0.52 *Rayleigh**(1/5) # Equation 9.32
        return Nu
    
    