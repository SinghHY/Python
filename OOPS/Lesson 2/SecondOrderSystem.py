class SecondOrderSystem:
    def __init__(self, wn: float, zeta: float) -> None:
        self.wn = wn
        self.zeta = zeta

    def damped_frequency(self) -> float:
        return self.wn * (1 - self.zeta ** 2) ** 0.5
    


system = SecondOrderSystem(wn=10, zeta=0.5)
print(f"Damped Frequency: {system.damped_frequency():.2f} rad/s")