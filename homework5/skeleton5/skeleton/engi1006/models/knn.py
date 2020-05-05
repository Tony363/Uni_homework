import numpy as np
import pandas as pd
from math import sqrt

from statistics import mode

def NNClassifier(training, testing, training_labels, testing_labels, k):
    '''Runs the Nearest Neighbor classifier:

    Args:
        training: the subset of data corresponding to the training data as a numpy matrix
        testing:  the subset of data corresponding to the testing data as a numpy matrix
        training_labels: the labels for the training data as a numpy array
        testing_labels: the labels for the testing data as a numpy array
        k: the number of nearest neighbors to use

    This function should do the following:

    - preallocate an array `labels` for the predicted labels of the testing data
    - for each row in the testing data, use knn to predict the label
    - at the end, return what percentagle of labels matched, i.e. how many labels in `labels` matched the label in `testing_labels`
    '''
    
    # preallocate labels
    labels = []
    # for each point
    for point in range(k):
        # run knn on each point and assign its label into labels
        labels.append(knn(training,training_labels,testing[point],k))
    # return % where prediction matched actual
    labels = np.ravel(labels)
    print(labels.size)
    print(testing_labels.size)
    return (labels == testing_labels).sum()/testing_labels.size


def knn(data, data_labels, vector, k):
    '''knn should calculate the nearest neighbor

    data: the numpy array of training data
    data_labels: the numpy array of labels for the training data
    vector: a row from the testing data to calculate nearest neighbors
    k: how many nearest neighbors to find


    This function should find the `k` nearest rows in `data` relative to
    `vector`, and take a vote amongst their labels. Whichever has more (b or m), return
    that value'''
    # preallocate distance array
    distance = []
    vote = []
    # for each point in data
    for point in data:
        # calculate the distance to vector, store in distance array
        distance.append(np.linalg.norm(point - vector))
    # sort distances, and get indexes to use in data_labels (look at np.argsort)
    distance = np.argsort(distance)
    # take vote amongs top labels
    for neighbor in range(k):
        
        index = distance[neighbor]
        vote.append(data_labels[index])
        # print(type(data_labels[index]))
        
    
    # print(vote)
    
    return vote
