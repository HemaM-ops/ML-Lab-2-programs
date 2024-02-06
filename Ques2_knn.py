import numpy as np
import heapq
import math

def euclidean_distance(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must have the same dimension")

    squared_diff = [(vec1[i] - vec2[i]) ** 2 for i in range(len(vec1))]
    return math.sqrt(sum(squared_diff))

def knn_classifier(train_data, train_labels, test_data, k):
    predictions = []
    for test_point in test_data:
        distances = [(euclidean_distance(test_point, train_point), label) for train_point, label in zip(train_data, train_labels)]
        k_nearest_neighbors = heapq.nsmallest(k, distances)
        neighbor_labels = [label for distance, label in k_nearest_neighbors]
        prediction = max(set(neighbor_labels), key=neighbor_labels.count)
        predictions.append(prediction)
    return predictions

# Generating random training and test data
np.random.seed(0)
train_data = np.random.rand(100, 5)  # 100 samples, 5 features
train_labels = np.random.randint(0, 2, 100)
test_data = np.random.rand(20, 5)  # 20 test samples

k = 3  #Number of neighbors
predictions = knn_classifier(train_data, train_labels, test_data, k)
print("Predictions:", predictions)
