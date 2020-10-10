"""
Preprocessed the microarray dataset
"""

import numpy as np
def preprocess(dataset_path):
    read_file = open(dataset_path, 'r');
    file_content = read_file.read();
    read_file.close();

    # Contains all N population in a list
    all_data = file_content.splitlines()


    individual_list = []        # Contains all the gene


    for lines in all_data:
        individual = []             # contains the values of individual
        values = lines.split()
        for i in values:
            int_i = float(i);   # convert string to integer
            individual.append(int_i)

        if (len(individual) > 0):
            individual_list.append(list(individual))  # Create a list that contains all the individual

    individual_length = len(individual_list[1])
    print (individual_length)
    



    #print individual_ref_id_list
    #print len(individual_ref_id_list) , len(individual_id_list1)
    return individual_length, individual_list


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





