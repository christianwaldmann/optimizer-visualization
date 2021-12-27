class Optimizer:
    def __init__(self, simulation, name="Unbekannter Optimierer"):
        self.simulation = simulation
        self.name = name
        self.position = simulation.getStartposition()

    def nextStepMonitored(self):
        if not self.simulation.getValues().isPositionOutOfBounds(self.position):
            self.nextStep()

    def nextStep(self):
        pass

    def getPosition(self):
        return self.position

    def getName(self):
        return self.name
