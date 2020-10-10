from nsga2.individual import Individual
import random

class Problem:

    def __init__(self, all_data_matrix, individual_no, objectives, num_of_variables, variables_range, expand=True, same_range=False):
        self.all_data_matrix = all_data_matrix
        self.individual_no = individual_no
        self.num_of_objectives = len(objectives)
        self.num_of_variables = num_of_variables
        self.objectives = objectives
        self.expand = expand
        self.variables_range = []
        if same_range:
            for _ in range(num_of_variables):
                self.variables_range.append(variables_range[0])
        else:
            self.variables_range = variables_range
        print (self.variables_range)
        exit()

    def generate_individual(self):
        xy = FCM(self.all_data_matrix,self.individual_no)
        center, u, d ,fpc, no_of_cluster, label = xy.FuzzyCMeans()             #Generate each individual using Fuzzy C means
        individual = Individual()
        individual.partition_matrix = u
        individual.distance_matrix = d
        individual.no_of_Cluster = no_of_cluster
        individual.fpc = fpc
        individual.labels= label
        #individual.BHI = self.zdt_definitions.BHI(individual)
        individual.features = []
        for sub_list in center:
                for feature in sub_list:
                    individual.features.append(feature)
        #print individual.no_of_Cluster , individual.features
        return individual

    def calculate_objectives(self, individual):
        if self.expand:
            individual.objectives = [f(*individual.features) for f in self.objectives]
        else:
            individual.objectives = [f(individual.features) for f in self.objectives]
