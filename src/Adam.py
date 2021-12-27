from src.Optimizer import Optimizer
from src.Position import Position
import numpy as np


class Adam(Optimizer):
    def __init__(self, simulation, alpha, beta1, beta2, epsilon):
        Optimizer.__init__(
            self,
            simulation,
            name=f"Adam $(\\alpha={alpha}, \\beta_1={beta1}, \\beta_2={beta2})$",
        )
        self.alpha = alpha
        self.beta1 = beta1
        self.beta2 = beta2
        self.v = np.array([0, 0])
        self.s = np.array([0, 0])
        self.epsilon = epsilon
        self.t = 1

    def nextStep(self):
        gradient = self.simulation.getValues().getGradientForPosition(self.position)
        self.v = self.beta1 * self.v + (1 - self.beta1) * gradient
        self.s = self.beta2 * self.s + (1 - self.beta2) * gradient * gradient
        vdach = self.v / (1 - self.beta1 ** self.t)
        sdach = self.s / (1 - self.beta2 ** self.t)
        w = self.position.getVec() - self.alpha * vdach / np.sqrt(sdach + self.epsilon)
        self.position = Position(vec=w)
        self.t += 1
