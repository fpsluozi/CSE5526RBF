# Neural Network Lab 2 for CSE5526 - RBF
This is a simple implementation of a single input and a single output 1-layer RBF network, using Gaussian kernels and K-Means in training. 
- The original function is h(x) = 0.5 * sin (2 * pi * x) + 0.4, x within [0.0, 1.0]
- The training data points are sampled with a +- 0.1 noise at h(x). 

# Dependence
Matplotlib is required in order to show the plots. If you only wish to see the features of the finalized clusters and the RBF network, run lab2-noplot.py instead.
# How to execute:
`python lab2.py [> rbf.log]`
OR  
`python lab2-noplot.py [> rbf.log]`
#How to configure:
Literally how to change the number of base functions, the learning rate and the variance determiner:  
1. Open lab2.py (or lab2-noplot.py) with your favorite text editor  
2. Change the value of K, ETA or MODE at the very beginning of the code, in the section "Environment Variables"  
3. Run it from command line again!  
4. Additional features: the number of training epoches and the number of sampled points are also customizeable. 
# File list:
- /src
	- lab2.py and lab2-noplot.py - The program launcher with the input data point sampler.
	- Approximator.py - The Gaussian cluster class and K-means cluster handlers.
	- Learner.py - The RBF network class with learning abilities.

- Readme.md 
