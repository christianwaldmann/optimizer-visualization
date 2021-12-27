from src.Optimizer import Optimizer
from src.Position import Position
import numpy as np


class GradientDescentMomentum(Optimizer):
    def __init__(self, simulation, alpha, beta):
        Optimizer.__init__(
            self, simulation, name=f"SGD Momentum $(\\alpha={alpha}, \\beta={beta})$"
        )
        self.alpha = alpha
        self.beta = beta
        self.v = np.array([0, 0])

    def nextStep(self):
        gradient = self.simulation.getValues().getGradientForPosition(self.position)
        self.v = self.beta * self.v + self.alpha * gradient
        w = self.position.getVec() - self.v
        self.position = Position(vec=w)
