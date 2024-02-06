import random
import math

def generate_random_vector(dim):
    return [random.randint(1, 100) for _ in range(dim)]  

def euclidean_distance(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must have the same dimension")

    squared_diff = [(vec1[i] - vec2[i]) ** 2 for i in range(len(vec1))]
    return math.sqrt(sum(squared_diff))

def manhattan_distance(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must have the same dimension")

    return sum(abs(vec1[i] - vec2[i]) for i in range(len(vec1)))


dim = random.randint(2, 10)  
vector1 = generate_random_vector(dim)
vector2 = generate_random_vector(dim)

print("Vector 1:", vector1)
print("Vector 2:", vector2)

euclidean_dist = euclidean_distance(vector1, vector2)
manhattan_dist = manhattan_distance(vector1, vector2)

print("Euclidean Distance:", euclidean_dist)
print("Manhattan Distance:", manhattan_dist)
