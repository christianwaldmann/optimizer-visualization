# Visualization of deep learning optimizers

This simulation visualizes gradient descent methods in different situations. The main motivation behind that is to better understand optimizers which are being used by deep learning frameworks.

![](animations/paraboladownwards3d.gif)

## Optimizers

All optimizers use the gradient for calculating their next step. In this simulation the gradient is calculated numerically ([symmetric derivative](https://en.wikipedia.org/wiki/Symmetric_derivative)).

The optimizers use the following formulas to calculate their next step:

![](optimizer_formulas.jpg)

## Scenes

### Local minimum

**3D View**
![](animations/localminimum3d.gif)

**Top-down view**
![](animations/localminimum.gif)

### Plateau

**3D View**
![](animations/plateau3d.gif)

**Top-down view**
![](animations/plateau.gif)

### Downwards parabola

**3D View**
![](animations/paraboladownwards3d.gif)

**Top-down view**
![](animations/paraboladownwards.gif)

### Hills

**3D View**
![](animations/hills3d.gif)

**Top-down view**
![](animations/hills.gif)

### Saddle point

**3D View**
![](animations/saddlepoint3d.gif)

**Top-down view**
![](animations/saddlepoint.gif)

### 5th degree polynom

**3D View**
![](animations/polynom53d.gif)

**Top-down view**
![](animations/polynom5.gif)
