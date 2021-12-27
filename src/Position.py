import numpy as np


class Position:
    def __init__(self, x=0, y=0, vec=None):
        # Set x, y directly
        self.x = x
        self.y = y
        # Or set x, y by numpy vector
        if hasattr(vec, "shape"):
            if vec.shape != (2,):
                raise ValueError("Invalid shape. Vector must have shape (2,)")
            self.x = vec[0]
            self.y = vec[1]

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __repr__(self):
        return f"{self.x}|{self.y}"

    def getVec(self):
        return np.array([self.x, self.y])
