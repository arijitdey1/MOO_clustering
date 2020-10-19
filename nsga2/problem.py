from nsga2.individual import Individual
from nsga2.clustering import CLUSTERING
import random

class Problem:

    def __init__(self, all_data_matrix, individual_no, objectives, expand=True, same_range=False):
        self.all_data_matrix = all_data_matrix
        self.individual_no = individual_no
        self.num_of_objectives = len(objectives)
        self.objectives = objectives
        self.expand = expand
        # self.variables_range = []
        # if same_range:
        #     for _ in range(num_of_variables):
        #         self.variables_range.append(variables_range[0])
        # else:
        #     self.variables_range = variables_range
        # print (self.variables_range)
        print ("Successful")

    def generate_individual(self):
        xy = CLUSTERING(self.all_data_matrix,self.individual_no)
        centroids, label, no_of_cluster = xy.kmeans()             #Generate each individual using k-means clustering
        individual = Individual()
        individual.no_of_Cluster = no_of_cluster
        individual.labels= label
        #individual.BHI = self.zdt_definitions.BHI(individual)
        individual.features = []
        for sub_list in centroids:
                for feature in sub_list:
                    individual.features.append(feature)
        print (individual.no_of_Cluster)
        return individual

    def calculate_objectives(self, individual):
        if self.expand:
            individual.objectives = [f(*individual.features) for f in self.objectives]
        else:
            individual.objectives = [f(individual.features) for f in self.objectives]
