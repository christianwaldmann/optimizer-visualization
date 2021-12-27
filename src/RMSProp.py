from src.Optimizer import Optimizer
from src.Position import Position
import numpy as np


class RMSProp(Optimizer):
    def __init__(self, simulation, alpha, beta, epsilon):
        Optimizer.__init__(
            self, simulation, name=f"RMSProp $(\\alpha={alpha}, \\beta={beta})$"
        )
        self.alpha = alpha
        self.beta = beta
        self.s = np.array([0, 0])
        self.epsilon = epsilon

    def nextStep(self):
        gradient = self.simulation.getValues().getGradientForPosition(self.position)
        self.s = self.beta * self.s + (1 - self.beta) * gradient * gradient
        w = self.position.getVec() - self.alpha * gradient / np.sqrt(
            self.s + self.epsilon
        )
        self.position = Position(vec=w)
