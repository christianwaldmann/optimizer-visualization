from src.Visualization import Visualization
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm
import glob
import os
import pathlib


class Visualization2D(Visualization):
    def __init__(self, sim, speed, createPngsForGif=False, showLevelValues=False):
        Visualization.__init__(self, sim, speed)
        self.hideAxis = True
        self.createPngsForGif = createPngsForGif
        if self.createPngsForGif:
            pathlib.Path("tmp").mkdir(exist_ok=True)
            for f in glob.glob("tmp/*.png"):
                os.remove(f)
        self.showLevelValues = showLevelValues
        self.animationIndex = 0

    def plotInitial(self):
        values = self.simulation.getValues()
        startposition = self.simulation.getStartposition()
        self.fig, self.ax = plt.subplots(figsize=(9, 9))
        cont = plt.contour(
            values.getX(), values.getY(), values.getZ(), levels=50, cmap=cm.jet
        )
        if self.showLevelValues:
            self.ax.clabel(cont)
        plt.scatter(
            startposition.getX(),
            startposition.getY(),
            marker="+",
            color="k",
            s=100,
            zorder=20,
        )
        positions = self.simulation.getPositions()
        self.sc = plt.scatter(
            [pos.getX() for pos in positions],
            [pos.getY() for pos in positions],
            color=self.colors[: len(positions)],
            s=100,
            alpha=1,
            edgecolors="k",
            zorder=10,
        )
        # Plot empty plots (n-1). This is needed for correct display of labels.
        # This is all done this way because we plot all data with a single scatter-call (in order to just update this in the update-function).
        # With this single scatter-call we can only add 1 label. To create the same effect as adding multiple labels, we create empty scatter-plots and add the labels at the legend-call
        for i in range(len(positions) - 1):
            plt.scatter(
                [],
                [],
                color=self.colors[i + 1],
                s=100,
                alpha=1,
                edgecolors="k",
                zorder=10,
            )
        names = self.simulation.getNames()
        plt.legend(["Start", *names], framealpha=1).set_zorder(100)
        plt.xlabel("x")
        plt.ylabel("y")
        if self.hideAxis:
            plt.axis("off")
        self.ani = animation.FuncAnimation(
            self.fig, self._update, interval=500 / self.speed, blit=True
        )

    def _getPositionForAnimation(self):
        if self.positionsListIndex < len(self.positionsList) - 1:
            self.positionsListIndex += 1
        else:
            self.positionsListIndex = 0
        return self.positionsList[self.positionsListIndex]

    def _update(self, i):
        self.sc.set_offsets(
            [(pos.getX(), pos.getY()) for pos in self._getPositionForAnimation()]
        )
        if self.createPngsForGif:
            plt.savefig(f"tmp/{self.animationIndex}.png")
        self.animationIndex += 1
        return (self.sc,)

    def show(self):
        # Plot trajectories
        for i in range(len(self.positions)):
            x = [step[i].getX() for step in self.positionsList]
            y = [step[i].getY() for step in self.positionsList]
            plt.plot(x, y, color=self.colors[i], linewidth=3, alpha=0.75)
        plt.show()
