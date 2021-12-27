from src.Subject import Subject


class Simulation(Subject):
    def __init__(self, nSteps, values=None, startposition=None):
        Subject.__init__(self)
        self.optimizers = []
        self.values = values
        self.startposition = startposition
        self.nOptimizer = 0
        self.nSteps = nSteps
        self.step = 0

    def loadScene(self, scene):
        self.startposition = scene.getStartposition()
        self.values = scene.getValues()

    def addOptimizer(self, opt):
        self.optimizers.append(opt)
        self.nOptimizer += 1

    def removeOptimizer(self, opt):
        self.optimizers.remove(opt)
        self.nOptimizer -= 1

    def nextStep(self):
        for opt in self.optimizers:
            opt.nextStepMonitored()
        self.notify()
        self.step += 1

    def getValues(self):
        return self.values

    def getPositions(self):
        return [opt.getPosition() for opt in self.optimizers]

    def getNames(self):
        return [opt.getName() for opt in self.optimizers]

    def getStartposition(self):
        return self.startposition

    def setStartposition(self, startposition):
        self.startposition = startposition

    def setNSteps(self, nSteps):
        self.nSteps = nSteps

    def getStep(self):
        return self.step

    def getNOptimizer(self):
        return self.nOptimizer

    def start(self):
        for _ in range(self.nSteps):
            self.nextStep()
