from src.ISubscriber import ISubscriber


class Visualization(ISubscriber):
    def __init__(self, sim, speed):
        self.simulation = sim
        self.colors = [
            "blue",
            "orange",
            "purple",
            "green",
            "yellow",
            "red",
            "lightseagreen",
            "black",
        ]
        self.speed = speed
        self.positionsList = [
            [
                self.simulation.getStartposition()
                for _ in range(self.simulation.getNOptimizer())
            ]
        ]
        self.positionsListIndex = 0

    def plotInitial(self):
        pass

    def update(self):
        self.positions = self.simulation.getPositions()
        self.positionsList.append(self.positions)

    def show(self):
        pass
