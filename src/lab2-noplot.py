# ====================================================================
# Title: CSE 5526 Autumn 2015 Lab 2 - RBF Network
# Author: Yiran Luo
# Last Updated: Oct 18, 2015
# Description: The program launcher without plot generator
# ====================================================================
# THE ENVIRONMENT VARIABLES
#
# CHANGE K, ETA AND MODE AS ARE REQUIRED.
# BUT NUM_SAMPLES AND NUM_EPOCHES ARE ALSO ADJUSTABLE.

K = 2 # The number of bases/clusters
ETA = 0.01 # The learning rate
MODE = 0 # The cluster variance mode. 0 for different variances and 
         # 1 for a single universal variance

NUM_SAMPLES = 75 # The number of sampled training data points.
NUM_EPOCHES = 100 # The number of epoches in training the RBF network.

# ====================================================================

import random
import math
from datetime import datetime
random.seed(datetime.now())
from Approximator import *
from Learner import *

sample_list = list()
sample_x_list = list()
sample_y_list = list()
sample_d_list = list()

def getH(x):    
    h = 0.5 + 0.4 * math.sin(2.0 * math.pi * x)
    return h

def getNoisedH(x):
    noise = random.uniform(-0.1, 0.1)
    h = getH(x) + noise
    return h

def getSamples(num=75):
    # Gets the training samples
    global sample_list 
    global sample_x_list 
    global sample_y_list
    global sample_d_list
    
    sample_list = list()
    sample_x_list = list()
    sample_y_list = list()
    sample_d_list = list()

    for i in range(num):
        x = random.random()
        h_x = getNoisedH(x)
        d = getH(x)

        sample_x_list.append(x)
        sample_y_list.append(h_x)
        sample_d_list.append(d)
        sample_list.append( (x, d) )


def run():
    global K
    global ETA
    global MODE
    global NUM_SAMPLES
    global NUM_EPOCHES

    getSamples(NUM_SAMPLES)

    print "======================" 
    print "BUILDING CLUSTERS..."
    cluster_list = list()
    init_cluster_list = getClusters(sample_x_list, K)
    final_cluster_list = updateClustersVariances(init_cluster_list, K, MODE)

    print "======================" 
    print "BUILDING RBF NETWORK..."
    print 
    learner = RBF(K)
    learner.updatePhi(final_cluster_list)
    learner.updateNetwork(sample_list, K, ETA, NUM_EPOCHES)
    print "RBF Weights:", learner.weight_list
    print "RBF Bias:", learner.b

    learned_y_list = list()
    for x in sample_x_list:
        learned_y_list.append(learner.getY(x))

    print "Finished."

run()
