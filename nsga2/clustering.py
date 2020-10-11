import numpy as np
import os
import skfuzzy as fuzz
import random

i = 0 ;
class CLUSTERING(object):

    def __init__(self,  all_data_matrix,individual_no):
        self.all_data_matrix = all_data_matrix
        self.individual_no = individual_no

    def FuzzyCMeans(self):
        x = random.randint(2,49)
        cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(self.all_data_matrix, x , 2, error=0.005, maxiter=10, init=None)
        label = np.argmax(u, axis=0)
        label_list= []
        for j in label:
            label_list.append(j)

        return cntr,u,d, fpc,x, label_list


        #print individual.features
