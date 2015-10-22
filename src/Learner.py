# ====================================================================
# Title: CSE 5526 Autumn 2015 Lab 2 - RBF Network
# Author: Yiran Luo
# Last Updated: Oct 18, 2015
# Description: The RBF network class with learning abilities.
# ==================================================================== 

import random
import math

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

class RBF:

    gaussian_list = list()
    weight_list = list()
    b = 0.0

    def __init__(self, k):
        # Initializes the weights and the bias with random numbers
        for i in range(k):
            self.weight_list.append(random.uniform(0.0, 0.5))
            self.b = random.uniform(0.0, 0.5)

    def getY(self, x):
        # Outputs the y from the final output neuron
        y = 0.0
        for i in range(len(self.gaussian_list)):
            y += self.gaussian_list[i].getGaussianValue(x) * self.weight_list[i]
        y += self.b
        return y

    def updatePhi(self, clusters):
        # Assigns the determined gaussian clusters to the network
        self.gaussian_list[:] = clusters[:]

    def updateNetwork(self, sample_list, k, eta, num_epoch = 100):
        
        for epoch in range(num_epoch):
            # In each epoch, we update the weights and the bias by each sample

            for sample in sample_list:
                current_x = sample[0]
                current_d = sample[1]
                e = current_d - self.getY(current_x)
                for j in range(k):
                    # The inputs of the output neuron come from the outputs of the phi's
                    current_phi_x = self.gaussian_list[j].getGaussianValue(current_x) 
                    self.weight_list[j] += eta * e * current_phi_x
                self.b += eta * e



