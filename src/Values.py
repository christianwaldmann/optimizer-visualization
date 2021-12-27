import numpy as np


class Values:
    def __init__(self, x, y, z, f):
        self.x = x
        self.y = y
        self.z = z
        self.f = f
        self.gradient = np.gradient(z)
        self.h = 1e-10

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def getGradientForPosition(self, position):
        x = position.getX()
        y = position.getY()
        grad_x = (self.f(x + self.h, y) - self.f(x - self.h, y)) / (2 * self.h)
        grad_y = (self.f(x, y + self.h) - self.f(x, y - self.h)) / (2 * self.h)
        return np.array([grad_x, grad_y])

    def getZForPosition(self, position):
        return self.f(position.getX(), position.getY())

    def isPositionOutOfBounds(self, position):
        if (
            position.getX() < np.min(self.x)
            or position.getX() > np.max(self.x)
            or position.getY() < np.min(self.y)
            or position.getY() > np.max(self.y)
        ):
            return True
        return False
