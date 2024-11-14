# src/data_processing/physics_data_visualizer.py

import numpy as np
import matplotlib.pyplot as plt

class PhysicsDataVisualizer:
    def __init__(self, equation):
        self.equation = equation

    def generate_wave_pattern(self, frequency, amplitude):
        """Generates a simple wave pattern."""
        x = np.linspace(0, 10, 100)
        y = amplitude * np.sin(frequency * x)
        plt.plot(x, y)
        plt.title("Wave Pattern")
        plt.show()

# Example usage
visualizer = PhysicsDataVisualizer("wave")
visualizer.generate_wave_pattern(frequency=2, amplitude=1)

