class PIDController:
    def __init__(self, kp: float, ki: float, kd: float) -> None:
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0.0
        self.prev_error = 0.0

    def compute(self, error: float, dt: float) -> float:
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.prev_error = error
        return output
    


pid = PIDController(kp=2.0, ki=0.1, kd=0.05)
error = 10.0  # Example error
dt = 0.1      # Time step
control_signal = pid.compute(error, dt)
print(f"Control Signal: {control_signal}")