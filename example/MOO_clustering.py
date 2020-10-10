import os, sys


from preprocessing.preprocessing import preprocess, preprocess_fcm_datamatrix
sys.path.append('../')

from nsga2.problem import Problem
from nsga2.evolution import Evolution
import matplotlib.pyplot as plt
import math

## Our objective functions

"""
Compute Fuzzy Partition Coefficient as f1
"""
def f1(self, individual):
	return individual.fpc

def f2(self, individual):
	individual_features = individual.features
	individual_length= int(len(individual_features)/individual.no_of_Cluster)
	centers = [individual_features[i:(i + individual_length)] for i in range(0, len(individual_features), individual_length)]
	distance_list = []
	for a, b in itertools.combinations(centers, 2):
		d1 = distance.euclidean(a, b)
		distance_list.append(d1)
	Dc = max(distance_list)
	Ec = np.sum(individual.partition_matrix * individual.distance_matrix)
	PBM_index = math.pow((Dc / (individual.no_of_Cluster * Ec)), 2)
	return PBM_index













individual_list = []

individual_length, individual_list = preprocess('Input_data/preprocessed_BCLL.txt')
all_data_matrix = preprocess_fcm_datamatrix( individual_length,individual_list)

print (individual_length)
print ("##", len(individual_list))


exit()
"""
Input from user
"""
chromosome_number = int(sys.argv[1])       # Enter the number of chromosome(individual) you want to generate
generation_number = int(sys.argv[2]) 
