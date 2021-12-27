# Visualization of deep learning optimizers

This simulation visualizes gradient descent methods in different situations. The main motivation behind that is to better understand optimizers which are being used by deep learning frameworks.

<img src="animations/paraboladownwards3d.gif">

## Optimizers

All optimizers use the gradient for calculating their next step. In this simulation the gradient is calculated numerically ([symmetric derivative](<[abc](https://en.wikipedia.org/wiki/Symmetric_derivative)>)).

The optimizers use the following formulas to calculate their next step:

### SGD

$$v = \alpha \cdot \nabla E(w)$$
$$w = w - v$$

### SGD Momentum

$$v = \beta \cdot v + \alpha \cdot \nabla E(w)$$
$$w = w - v$$

### Nesterov Momentum

$$v = \beta \cdot v + \alpha \cdot \nabla E(w - \beta \cdot v)$$
$$w = w - v$$

### AdaGrad

$$s = s + \nabla E(w) \otimes \nabla E(w)$$
$$w = w - \alpha \cdot \nabla E(w) \oslash \sqrt{s + \epsilon}$$

### RMSProp

$$s = \beta \cdot s + (1 - \beta) \cdot \nabla E(w) \otimes \nabla E(w)$$
$$w = w - \alpha \cdot \nabla E(w) \oslash \sqrt{s + \epsilon}$$

### Adam

$$v = \beta_1 \cdot v + (1 - \beta_1) \cdot \nabla E(w)$$
$$s = \beta_2 \cdot s + (1 - \beta_2) \cdot \nabla E(w) \otimes \nabla E(w)$$
$$\hat v = \frac{v}{1 - \beta_1^t}$$
$$\hat s = \frac{s}{1 - \beta_2^t}$$
$$w = w - \alpha \cdot \hat v \oslash \sqrt{\hat s + \epsilon}$$

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
