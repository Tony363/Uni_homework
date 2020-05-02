from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


def SKLearnKnnClassifier(training, testing, training_labels, testing_labels, k):
    '''leverage Scikit-learn to implement the k nearest neighbors algorithm
    Args:
        training: the subset of data corresponding to the training data as a numpy matrix
        testing:  the subset of data corresponding to the testing data as a numpy matrix
        training_labels: the labels for the training data as a numpy array
        testing_labels: the labels for the testing data as a numpy array
        k: the number of nearest neighbors to use

    This should instantiate the class from scikit learn, then call
    `.fit` and `.predict`. It should then compare results similar to
    NNClassifier to return a % correct.
    
    See how easy it is to use scikit learn?
    '''
    # instantiate model
    knn = KNeighborsClassifier(n_neighbors=k,metric='euclidean')
    # fit model to training data
    print(training.shape)
    print(testing.shape)
    print(training_labels.shape)
    print(testing_labels.shape)
    knn.fit(training,training_labels)
    # predict test labels
    y_pred = knn.predict([testing_labels])
    # return % where prediction matched actual
    return round((y_pred/testing_labels) * 100,2)

def SKLearnSVMClassifier(training, testing, training_labels, testing_labels):
    '''leverage Scikit-learn to implement the support vector machine classifier
    Args:
        training: the subset of data corresponding to the training data as a numpy matrix
        testing:  the subset of data corresponding to the testing data as a numpy matrix
        training_labels: the labels for the training data as a numpy array
        testing_labels: the labels for the testing data as a numpy array

    This should instantiate the class from scikit learn, then call
    `.fit` and `.predict`. It should then compare results similar to
    NNClassifier to return a % correct.
    
    See how easy it is to use scikit learn?
    '''
    # instantiate model
    clf = SVC(gamma='auto')
    # fit model to training data
    clf.fit(training,training_labels)
    # predict test labels
    y_pred = clf.predict(testing_labels)
    # return % where prediction matched actual
    return round((y_pred/testing_labels) * 100,2)
