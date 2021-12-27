from src.Visualization import Visualization
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d.art3d import juggle_axes
from matplotlib import cm
import glob
import os
import pathlib


class Visualization3D(Visualization):
    def __init__(self, sim, speed, createPngsForGif=False):
        Visualization.__init__(self, sim, speed)
        self.hideAxis = True
        self.createPngsForGif = createPngsForGif
        if self.createPngsForGif:
            pathlib.Path("tmp").mkdir(exist_ok=True)
            for f in glob.glob("tmp/*.png"):
                os.remove(f)
        self.animationIndex = 0

    def plotInitial(self):
        values = self.simulation.getValues()
        startposition = self.simulation.getStartposition()
        self.fig = plt.figure(figsize=(9, 9))
        plt.axes(projection="3d")
        self.ax = plt.gca()
        # surf = self.ax.plot_surface(
        #     werte.getX(),
        #     werte.getY(),
        #     werte.getZ(),
        #     cmap=cm.jet,
        #     shade=True,
        #     zorder=1,
        # )
        # surf._facecolors2d = surf._facecolor3d
        # surf._edgecolors2d = surf._edgecolor3d
        self.ax.contour(
            values.getX(),
            values.getY(),
            values.getZ(),
            levels=50,
            cmap=cm.jet,
            alpha=0.7,
            zorder=1,
        )
        self.ax.scatter(
            startposition.getX(),
            startposition.getY(),
            values.getZForPosition(startposition),
            marker="+",
            color="k",
            s=100,
            zorder=20,
        )
        positions = self.simulation.getPositions()
        self.sc = self.ax.scatter(
            [pos.getX() for pos in positions],
            [pos.getY() for pos in positions],
            [values.getZForPosition(pos) for pos in positions],
            color=self.colors[: len(positions)],
            s=100,
            alpha=1,
            edgecolors="k",
            zorder=11,
        )
        # Plot empty plots (n-1). This is needed for correct display of labels.
        # This is all done this way because we plot all data with a single scatter-call (in order to just update this in the update-function).
        # With this single scatter-call we can only add 1 label. To create the same effect as adding multiple labels, we create empty scatter-plots and add the labels at the legend-call
        for i in range(len(positions) - 1):
            self.ax.scatter(
                [],
                [],
                [],
                color=self.colors[i + 1],
                s=100,
                alpha=1,
                edgecolors="k",
                zorder=11,
            )
        plt.legend(["Start", *self.simulation.getNames()], framealpha=1).set_zorder(100)
        plt.xlabel("x")
        plt.ylabel("y")
        if self.hideAxis:
            plt.axis("off")
        self.ani = animation.FuncAnimation(
            self.fig, self._update, interval=100 / self.speed, blit=False
        )

    def _getPositionForAnimation(self):
        if self.positionsListIndex < len(self.positionsList) - 1:
            self.positionsListIndex += 1
        else:
            self.positionsListIndex = 0
        return self.positionsList[self.positionsListIndex]

    def _update(self, i):
        positions = self._getPositionForAnimation()
        values = self.simulation.getValues()
        self.sc._offsets3d = juggle_axes(
            [pos.getX() for pos in positions],
            [pos.getY() for pos in positions],
            [values.getZForPosition(pos) for pos in positions],
            "z",
        )
        if self.createPngsForGif:
            plt.savefig(f"tmp/{self.animationIndex}.png")
        self.animationIndex += 1
        return (self.sc,)

    def show(self):
        # Plot trajectories
        values = self.simulation.getValues()
        for i in range(len(self.positions)):
            x = [step[i].getX() for step in self.positionsList]
            y = [step[i].getY() for step in self.positionsList]
            z = [values.getZForPosition(step[i]) for step in self.positionsList]
            self.ax.plot(
                x, y, z, color=self.colors[i], linewidth=3, alpha=0.75, zorder=10
            )
        plt.show()
