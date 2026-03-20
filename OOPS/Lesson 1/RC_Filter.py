class RC_Filter():
    def __init__(self, resistance:float, capacitance:float) -> None:
        self.resistance = resistance
        self.capacitance = capacitance
        
    def time_constant(self):
        return(self.resistance * self.capacitance)
        
    def cutoff_frequency(self):
        return(1 / (2 * 3.14159 * self.time_constant()))
    
filt = RC_Filter(1000, 1e-6)
print(filt.time_constant())
print(filt.cutoff_frequency())