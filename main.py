from src.Simulation import Simulation
from src.Visualization2D import Visualization2D
from src.Visualization3D import Visualization3D
from src.OutputPrinter import OutputPrinter
from src.GradientDescent import GradientDescent
from src.GradientDescentMomentum import GradientDescentMomentum
from src.NesterovMomentum import NesterovMomentum
from src.AdaGrad import AdaGrad
from src.RMSProp import RMSProp
from src.Adam import Adam
from src.Scene import (
    paraboladownwards,
    parabola,
    hills,
    polynom5,
    plateau,
    localminimum,
    saddlepoint,
    bowl,
    beale,
)
import matplotlib.pyplot as plt


# Parameters
nSteps = 750
visualisation = "3D"  # '2D' or '3D'
animationspeed = 5
epsilon = 1e-8
createPngsForGif = False  # Clears /tmp first and then saves every frame of the animation as .png in /tmp until the script is stopped


# Initialize simulation and load scene
sim = Simulation(nSteps=nSteps)
sim.loadScene(paraboladownwards)


# Initialize optimizers
sgd = GradientDescent(sim, alpha=0.01)
sgdmom = GradientDescentMomentum(sim, alpha=0.01, beta=0.9)
nesterov = NesterovMomentum(sim, alpha=0.01, beta=0.9)
adagrad = AdaGrad(sim, alpha=0.2, epsilon=epsilon)
rmsprop = RMSProp(sim, alpha=0.05, beta=0.9, epsilon=epsilon)
adam = Adam(sim, alpha=0.05, beta1=0.9, beta2=0.999, epsilon=epsilon)


# Add optimizers to simulation
sim.addOptimizer(sgd)
sim.addOptimizer(sgdmom)
sim.addOptimizer(nesterov)
sim.addOptimizer(adagrad)
sim.addOptimizer(rmsprop)
sim.addOptimizer(adam)


# Initialize simulation observers
if visualisation == "3D":
    vis = Visualization3D(sim, animationspeed, createPngsForGif)
else:
    vis = Visualization2D(sim, animationspeed, createPngsForGif)
out = OutputPrinter(sim)


# Add observers to simulation
sim.subscribe(vis)
sim.subscribe(out)


# Create plot
vis.plotInitial()
# plt.gca().view_init(azim=47, elev=35)  # May be needed when creating gifs for 3D view
# plt.gca().dist = 7


# Start simulation
sim.start()


# Display plot
vis.show()
