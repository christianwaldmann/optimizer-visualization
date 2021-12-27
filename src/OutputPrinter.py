from src.ISubscriber import ISubscriber


class OutputPrinter(ISubscriber):
    def __init__(self, sim):
        self.simulation = sim

    def update(self):
        if self.simulation.getStep() % 10 == 0:
            print(f"Step {self.simulation.getStep():4} | ", end="")
            names = self.simulation.getNames()
            positions = self.simulation.getPositions()
            for name, pos in zip(names, positions):
                print(f"{name}: ({pos.getX():5.2f},{pos.getY():4.2f}) | ", end="")
            print()
