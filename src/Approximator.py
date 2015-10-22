# ====================================================================
# Title: CSE 5526 Autumn 2015 Lab 2 - RBF Network
# Author: Yiran Luo
# Last Updated: Oct 18, 2015
# Description: The Gaussian Cluster and its handling functions
# ====================================================================

import random
import math
from datetime import datetime
random.seed(datetime.now())

def getDistanceSquared(x, y):
    # Assume x and y are both 1-d
    return (x - y)**2

class Gaussian:
    
    def __init__(self, center):
        self.variance = 0.5 # The sigma^2
        self.center = center # The mu
        
    def getGaussianValue(self, x):
        return math.exp(-0.5 / self.variance * getDistanceSquared(x, self.center))

class Cluster(Gaussian):

    member_list = list()

    def clearMember(self):
        self.member_list = list()

    def hasMoreThanOne(self):
        return len(self.member_list) > 1

    def updateCenter(self):
        if len(self.member_list) > 0:
            new_center = sum(self.member_list) / len(self.member_list)
            
            # While updating the center, it also verifies if this cluster has converged
            if new_center == self.center:
                is_converged = True
            else:
                is_converged = False
                self.member_list = list()
            self.center = new_center
            return is_converged
        else:
            return True

    def updateVariance(self, avg_variance=0.5):
        if len(self.member_list) <= 1:
            self.variance = avg_variance
        else:
            s = 0.0
            for x in self.member_list:
                s += getDistanceSquared(x, self.center)
            self.variance = s / float(len(self.member_list))

    def getDistanceToCenter(self, x):
        return getDistanceSquared(x, self.center)

    def printInfo(self):
        print "Cluster center at", self.center
        print "Cluster variance", self.variance
        print 

def getClusters(sample_x_list, k):
    # Relocates the clusters using K-Means

    cluster_list = list()
    # The initial centers are chosen from the samples
    init_center_list = random.sample(sample_x_list, k)
    for x in range(k):
        new_cluster = Cluster(init_center_list[x])
        cluster_list.append(new_cluster)
       
    clusters_converged = False
        
    while not clusters_converged:
        for i in range(len(sample_x_list)):
            
            # Finds the closest cluster for each sample
            cluster_distance_list = list()
            current_x = sample_x_list[i]

            # Pushes the distance to each cluster into cluster_distance_list
            for c in cluster_list:
                distance_to_c = c.getDistanceToCenter(current_x)
                cluster_distance_list.append(distance_to_c)

            # Gets the index of the closest cluster
            closest_cluster_index = cluster_distance_list.index(min(cluster_distance_list))
            cluster_list[closest_cluster_index].member_list.append(current_x)
        
        # Verifies if all clusters have converged
        clusters_converged = True
        for c in cluster_list:
            clusters_converged = clusters_converged and c.updateCenter()
        
        if not clusters_converged:
            for c in cluster_list:
                c.clearMember()
            
    return cluster_list
    
def updateClustersVariances(clusters, k, mode=0):
    # Sets the clusters' variances after they are finalized

    cluster_list = list()
    cluster_list[:] = clusters[:]
    if mode == 0:
        # The straightforward variance update
        # In case a cluster has no more than 1 member      
        num_legit_clusters = k
        
        sum_variances = 0.0
        for c in cluster_list:
            if c.hasMoreThanOne:
                c.updateVariance()
                sum_variances += c.variance
            else:
                num_legit_clusters -= 1
        print
        print "Using independent cluster variances"
        print "Number of clusters with more than one member:", num_legit_clusters
        mean_variance = sum_variances / num_legit_clusters
        for c in cluster_list:
            if not c.hasMoreThanOne:
                c.updataVariance(mean_variance)
        
    else:
        # The simplified varaince update
        # Using the universal variance for all the clusters
        # variance = d_max^2 / 2K
        
        center_distance_list = list()
        for ci in cluster_list:
            for cj in cluster_list:
                center_distance_list.append(getDistanceSquared(ci.center, cj.center))
        d_max_squared = max(center_distance_list)
        print
        print "Using the universal cluster variance."
        print "Maximum distance between cluster centers is:", math.sqrt(d_max_squared)
        max_variance = d_max_squared / (2.0 * k)
        for c in cluster_list:
            c.variance = max_variance

    print "======================" 
    print "FINALIZED CLUSTERS:\n"
    for x in cluster_list:
        x.printInfo()

    return cluster_list

