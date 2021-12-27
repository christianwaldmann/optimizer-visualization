from src.Optimizer import Optimizer
from src.Position import Position
import numpy as np


class NesterovMomentum(Optimizer):
    def __init__(self, simulation, alpha, beta):
        Optimizer.__init__(
            self,
            simulation,
            name=f"Nesterov Momentum $(\\alpha={alpha}, \\beta={beta})$",
        )
        self.alpha = alpha
        self.beta = beta
        self.v = np.array([0, 0])

    def nextStep(self):
        new_position_vec = self.position.getVec() - self.beta * self.v
        gradient = self.simulation.getValues().getGradientForPosition(
            Position(vec=new_position_vec)
        )
        self.v = self.beta * self.v + self.alpha * gradient
        w = self.position.getVec() - self.v
        self.position = Position(vec=w)
