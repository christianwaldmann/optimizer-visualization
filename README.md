# Visualization of deep learning optimizers

This simulation visualizes gradient descent methods in different situations. The main motivation behind that is to better understand optimizers which are being used by deep learning frameworks.

<img src="animations/paraboladownwards3d.gif">

## Optimizers

All optimizers use the gradient for calculating their next step. In this simulation the gradient is calculated numerically ([symmetric derivative](<[abc](https://en.wikipedia.org/wiki/Symmetric_derivative)>)).

The optimizers use the following formulas to calculate their next step:

![](optimizer_formulas.jpg)

## Scenes

### Local minimum

**3D View**
<img src="animations/localminimum3d.gif">

**Top-down view**
<img src="animations/localminimum.gif">

### Plateau

**3D View**
<img src="animations/plateau3d.gif">

**Top-down view**
<img src="animations/plateau.gif">

### Downwards parabola

**3D View**
<img src="animations/paraboladownwards3d.gif">

**Top-down view**
<img src="animations/paraboladownwards.gif">

### Hills

**3D View**
<img src="animations/hills3d.gif">

**Top-down view**
<img src="animations/hills.gif">

### Saddle point

**3D View**
<img src="animations/saddlepoint3d.gif">

**Top-down view**
<img src="animations/saddlepoint.gif">

### 5th degree polynom

**3D View**
<img src="animations/polynom53d.gif">

**Top-down view**
<img src="animations/polynom5.gif">
