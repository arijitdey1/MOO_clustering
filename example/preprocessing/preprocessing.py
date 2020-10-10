"""
Preprocessed the microarray dataset
"""
from function import is_number
import numpy as np
def preprocess(dataset_path):
    read_file = open(dataset_path, 'r');
    write_file_population = open('Intermediate_Data/Initial_population.txt', 'w')
    write_file_population_id = open('Intermediate_Data/population_id.txt', 'w')
    file_content = read_file.read();
    read_file.close();

    # Contains all N population in a list
    all_data = file_content.splitlines()

    individual_list = []        # Contains all the gene


    for lines in all_data:
        individual = []             # contains the values of individual
        individual_id = [];         # contains the id values of individual
        values = lines.split()
        for i in values:
            if (is_number(i) == 1):
                int_i = float(i);   # convert string to integer
                individual.append(int_i)
            else:
                individual_id.append(i.upper())

        if (len(individual) > 0):
            individual_list.append(list(individual))  # Create a list that contains all the individual
        if (len(individual_id) > 0):
            individual_id_list.append(list(individual_id[0:1]))
            individual_ref_id.append(list(individual_id[1:2]))

    individual_length = len(individual_list[1])
    #print individual_length

    for item in individual_list:
        write_file_population.write("%s \n" % item)

    individual_id_list1 = []
    individual_ref_id_list = []
    for item in individual_ref_id:
        for x in item:
            individual_ref_id_list.append(x)
    for item in individual_id_list:
        for x in item:
            individual_id_list1.append(x)
            write_file_population_id.write("%s \n" % x)

    #print individual_ref_id_list
    #print len(individual_ref_id_list) , len(individual_id_list1)
    return individual_length, individual_list, individual_id_list1, individual_ref_id_list


def preprocess_fcm_datamatrix(individual_len, individual_list):
    datapnts_list = []
    #print individual_len
    for list in range(individual_len):  # create list of list that contains 21 list to contain all 21 dimension datpoints
        datapnts_list.append([])

    '''
    Generate 2D matrix that can be fed to FCM algorithm
    '''
    all_data = []
    for cols in range(individual_len):
        for rows in individual_list:
            datapnts_list[cols] = np.hstack((datapnts_list[cols], rows[cols]))
        all_data.append(datapnts_list[cols])
    all_data_matrix = np.vstack((all_data))
    np.savetxt('Intermediate_Data/matrix_data.txt', all_data_matrix, fmt='%-7.2f')
    return all_data_matrix





