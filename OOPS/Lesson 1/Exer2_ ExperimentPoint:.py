class ExperimentPoint:
    def __init__(self, time, input_signal, output_signal)-> None:
        self.time = time
        self.input_signal = input_signal
        self.output_signal = output_signal
        
    def Error(self):
        return self.input_signal - self.output_signal
    
total_error = ExperimentPoint(0.1, 50, 30)
print(total_error.Error())