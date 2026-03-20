class MassSpringDamper:
    def __init__(self, mass: float, damping: float, stiffness: float) -> None:
        self.mass = mass
        self.damping = damping
        self.stiffness = stiffness

    def natural_frequency(self) -> float:
        return (self.stiffness / self.mass) ** 0.5

    def damping_ratio(self) -> float:
        return self.damping / (2 * (self.mass * self.stiffness) ** 0.5)
    
    
system = MassSpringDamper(mass=2.0, damping=1.2, stiffness=50.0)

print(system.natural_frequency())
print(system.damping_ratio())