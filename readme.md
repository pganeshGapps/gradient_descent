## Gradient Descent Example for Linear Regression
This example project demonstrates how the [gradient descent](http://en.wikipedia.org/wiki/Gradient_descent) algorithm may be used to solve a [linear regression](http://en.wikipedia.org/wiki/Linear_regression) problem. 

### Code Requirements
 Python ([version 3.5](https://www.python.org/doc/versions/) or higher will work). 
 Only other requirement is [NumPy](http://www.numpy.org/).

### Description
This code demonstrates how a gradient descent search may be used to solve the 'Linear Regression' problem of fitting a line to a set of points. In this problem, we wish to model a set of points using a line. The line model is defined by two parameters - the line's slope `m`, and y-intercept `b`. Gradient descent attemps to find the best values for these parameters, subject to an error function.

The code contains a main function called `run`. This function defines a set of parameters used in the gradient descent algorithm including an initial guess of the line slope and y-intercept, the learning rate to use, and the number of iterations to run gradient descent for. 

*Note for choosing 'iterations':*

Choose number of iterations just greater than i,where delta(change in error) becomes less than some acceptable change in error(e.g.10e-5).

*Note for choosing 'learning_rate(@)':*

Consider following points while choosing 'learning_rate':

	1.If @ is too small, then your Gradient Descent Algo.(GDA) can become slow.

	2.If @ is too big, then your GDA may :

		a)overshoot the minimum

		b)may not converge or may diverge.

There also an emerging method (which I haven’t tried but looks promising) to use learned features to predict learning rates of gradient descent. Go through this [paper](https://arxiv.org/abs/1606.04474) for more details.

```python
initial_b = 0 # initial y-intercept guess
initial_m = 0 # initial slope guess
num_iterations = 1000 
``` 

Using these parameters a gradient descent search is executed on a sample data set of 100 ponts. 
Here is a example of the search running for 270 iterations using an initial guess of `m = 0`, `b = 0`, and a learning rate of `0.00005`.

<img src="https://github.com/pganeshGapps/gradient_descent/blob/master/plot_01.png" width="580">

### Execution

```
python gradient_descent.py
```

The output will look like this

```
Starting gradient descent at b = 0, m = 0, error = 5565.107834483211
Running...
Runner completed its job.
Delta=1.8027214323979024e-05, iterations=270
After 270 iterations b = 0.037176415932999606, m = 1.478761414262951, error = 112.64579441603475
```
OR

```
Starting gradient descent at b = 0, m = 4.1, error = 17218.283231195655
Running...
Runner completed its job.
Delta=1.8393831581420272e-05, iterations=270
After 270 iterations b = -0.043294679012631294, m = 1.4803430491155023, error = 112.69436722916174

```

A more detailed description of this example can be found in following references:

### References

1.Refer [this](https://arxiv.org/abs/1609.04747) paper on overview of gradient descent optimization algorithms.

2.CS231n [Course material](http://cs231n.github.io/neural-networks-3/) on gradient descent.

3.Chapter 4 (Numerical optimization) and Chapter 8 (Optimization for Deep Learning models) of Deep Learning book.