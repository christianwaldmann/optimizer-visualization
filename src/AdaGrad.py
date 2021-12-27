from src.Optimizer import Optimizer
from src.Position import Position
import numpy as np


class AdaGrad(Optimizer):
    def __init__(self, simulation, alpha, epsilon):
        Optimizer.__init__(self, simulation, name=f"AdaGrad $(\\alpha={alpha})$")
        self.alpha = alpha
        self.s = np.array([0, 0])
        self.epsilon = epsilon

    def nextStep(self):
        gradient = self.simulation.getValues().getGradientForPosition(self.position)
        self.s = self.s + gradient * gradient
        w = self.position.getVec() - self.alpha * gradient / np.sqrt(
            self.s + self.epsilon
        )
        self.position = Position(vec=w)
