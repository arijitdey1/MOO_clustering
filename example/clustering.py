import os, sys


from preprocessing.preprocessing import preprocess, preprocess_fcm_datamatrix,AnnotatedClustering , Confidence_Score_Matrix
sys.path.append('../')

from nsga2.problem import Problem
from nsga2.evolution import Evolution
import matplotlib.pyplot as plt
import math

individual_list = []

individual_length, individual_list , individual_id_list , individual_ref_id_list = preprocess('Input_data/preprocessed_BCLL.txt')
all_data_matrix , all_normalized_data_matrix = preprocess_fcm_datamatrix( individual_length,individual_list)

print (all_data_matrix)

exit()
"""
Input from user
"""
chromosome_number = int(sys.argv[1])       # Enter the number of chromosome(individual) you want to generate
generation_number = int(sys.argv[2]) 
