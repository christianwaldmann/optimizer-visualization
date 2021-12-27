from src.Optimizer import Optimizer
from src.Position import Position


class GradientDescent(Optimizer):
    def __init__(self, simulation, alpha):
        Optimizer.__init__(self, simulation, name=f"SGD $(\\alpha={alpha})$")
        self.alpha = alpha

    def nextStep(self):
        gradient = self.simulation.getValues().getGradientForPosition(self.position)
        v = self.alpha * gradient
        w = self.position.getVec() - v
        self.position = Position(vec=w)
