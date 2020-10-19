import os, sys


from preprocessing.preprocessing import preprocess, preprocess_fcm_datamatrix
sys.path.append('../')

from nsga2.problem import Problem
from nsga2.evolution import Evolution
import matplotlib.pyplot as plt
import math
import numpy as np
from sklearn.cluster import KMeans


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
data_matrix_trans = preprocess_fcm_datamatrix( individual_length,individual_list)
individual_no = len(individual_list)
data_matrix= np.array(individual_list)
print ("##",data_matrix.shape)
print (data_matrix_trans.shape)



"""
Input from user
"""
chromosome_number = int(sys.argv[1])       # Enter the number of chromosome(individual) you want to generate
generation_number = int(sys.argv[2]) 

#problem = Problem(num_of_variables=3, objectives=[f1, f2], variables_range=[(-5, 5)], same_range=True, expand=False)
#all_data_matrix, individual_no, objectives, num_of_variables, variables_range, expand=True, same_range=False
problem = Problem(data_matrix, individual_no, objectives= [f1, f2], expand=True, same_range=False)
problem.generate_individual()