from src.Position import Position
from src.Values import Values
import numpy as np


# TODO: https://en.wikipedia.org/wiki/Test_functions_for_optimization


class Scene:
    def __init__(self, startposition, x, y, f):
        self.startposition = startposition
        x, y = np.meshgrid(x, y)
        f_vec = np.vectorize(f)
        z = f_vec(x, y)
        self.values = Values(x, y, z, f)

    def getStartposition(self):
        return self.startposition

    def getValues(self):
        return self.values


hills = Scene(
    startposition=Position(3.0, 2.7),
    x=np.linspace(-3.5, 3.5, 200),
    y=np.linspace(-3.5, 3.5, 200),
    f=lambda x, y: 2 * np.exp(-((x - 1) * (x - 1) + y * y) / 0.2)
    + 6.0 * np.exp(-((x + 1) * (x + 1) + y * y) / 0.2)
    - 2 * np.exp(-((x - 1) * (x - 1) + (y + 1) * (y + 1)) / 0.2)
    + x * x
    + y * y,
)


polynom5 = Scene(
    startposition=Position(0, 0.5),
    x=np.linspace(-3.5, 3.5, 200),
    y=np.linspace(-3.5, 3.5, 200),
    f=lambda x, y: (
        (x + 4) * (x + 2) * (x + 1) * (x - 1) * (x - 3)
        + (y + 4) * (y + 2) * (y + 1) * (y - 1) * (y - 3)
    )
    / 10,
)


parabola = Scene(
    startposition=Position(0.3, 2.5),
    x=np.linspace(-3.5, 3.5, 200),
    y=np.linspace(-3.5, 3.5, 200),
    f=lambda x, y: x * x + y * y,
)


paraboladownwards = Scene(
    startposition=Position(-2.3, -1.59),
    x=np.linspace(-3.5, 3.5, 200),
    y=np.linspace(-3.5, 3.5, 200),
    f=lambda x, y: x * x - y * y - 3.2 * y,
)


def _plateau_f(x, y):
    x *= 10
    y *= 10
    r = np.sqrt(x * x + y * y) + 0.01
    return -np.sin(r) / r + 0.01 * r * r


plateau = Scene(
    startposition=Position(0.3, 2.5),
    x=np.linspace(-3.5, 3.5, 200),
    y=np.linspace(-3.5, 3.5, 200),
    f=_plateau_f,
)


saddlepoint = Scene(
    startposition=Position(np.pi / 2 - 0.1, 2.5),
    x=np.linspace(-3.5, 3.5, 200),
    y=np.linspace(-3.5, 3.5, 200),
    f=lambda x, y: np.sin(x) + y * y,
)


def _bowl_f(x, y):
    x /= 2
    y /= 2
    return -np.exp(-(x * x + 5 * y * y)) + x * x + 0.5 * y * y


bowl = Scene(
    startposition=Position(np.pi / 2 - 0.1, 2.5),
    x=np.linspace(-3.5, 3.5, 200),
    y=np.linspace(-3.5, 3.5, 200),
    f=_bowl_f,
)


def _localminimum_f(x, y):
    y *= 1.4
    return (
        -2 * np.exp(-((x - 1) * (x - 1) + y * y) / 0.2)
        - 6.0 * np.exp(-((x + 1) * (x + 1) + y * y) / 0.2)
        + x * x
        + y * y
    )


localminimum = Scene(
    startposition=Position(np.pi / 2 - 0.1, 2.5),
    x=np.linspace(-3.5, 3.5, 200),
    y=np.linspace(-3.5, 3.5, 200),
    f=_localminimum_f,
)


beale = Scene(
    startposition=Position(1, 2),
    x=np.linspace(-4.5, 4.5, 200),
    y=np.linspace(-4.5, 4.5, 200),
    f=lambda x, y: (
        (1.5 - x + x * y) ** 2
        + (2.25 - x + x * y ** 2) ** 2
        + (2.625 - x + x * y ** 3) ** 2
    )
    / 1000000,
)
