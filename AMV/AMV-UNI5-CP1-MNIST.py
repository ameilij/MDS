# LA CIENCIA DE DATOS
# TECNICAS DE VISUALIZACION, MINERIA Y ANALISIS
# UNIDAD 5 MODELOS
# Caso Practico 1

# Import relevant libraries
import pyarrow.parquet as pq
import numpy as np
import pandas as pd
import pyarrow as pa
from numpy.core._multiarray_umath import ndarray

# FUNCTION DEFINITION AREA

def transform_clean_format(image_set_instance):
    """Transform an image to a CLEAN_FORMAT, which is an image of 28x28 zeros or ones.
    This simplifies a lot calculating actual space used by a pic regardless or value.

    :parameter image_set_instance

    :return image_clean_format
    """
    temp = image_set_instance.to_list()
    temp2 = [1 if valores > 0 else 0 for valores in temp]
    image_clean_format: ndarray = np.reshape(temp2, (28, 28))
    return image_clean_format

def calculate_horizontal_density(some_image_matrix):
    """Calculate the average pixel density for the 28 rows in an image matrix
    :parameter
    some_image_matrix

    :return
    row_density_counter
    """
    row_density_counter = []
    for rows in some_image_matrix:
        temp = sum(rows)/len(rows)
        row_density_counter.append(temp)
    return np.mean(row_density_counter)

def get_class_average_horizontal_density(image_set, class_set, target):
    """Get a target class, evaluate all elements, and return average
    horizontal density of row for that class

    :parameter image_set
    :parameter class_set
    :parameter target

    :return class_average_horizontal_density_list MEAN
    :return class_average_horizontal_density_list SD
    :return counter_evaluation
    """
    class_average_horizontal_density_list = []
    counter_evaluation = 0

    for i in range(1, len(image_set)):
        if (class_set[i] == target):
            reduced_image_set = transform_clean_format(image_set.iloc[i])
            temp = calculate_horizontal_density(reduced_image_set)
            class_average_horizontal_density_list.append(temp)
            counter_evaluation = counter_evaluation + 1

    return(np.mean(class_average_horizontal_density_list), np.std(class_average_horizontal_density_list), counter_evaluation)

def classifier(image):
    """Simple classification model that analyzes if horizontal density of an image
    belongs to that trained for zeroes or ones. Function assumes that information in
    image is either one or zero, not any other number.

    :parameter image

    :return prediction
    """

    # Model parameters for ZERO classification
    zero_mean = 0.24460545843717754
    zero_sd = 0.0429571657861942
    zero_ub = zero_mean + (3 * zero_sd)
    zero_lb = zero_mean - (3 * zero_sd)

    # Model parameters for ONE classification
    one_mean = 0.1095654683099595
    one_sd = 0.025619148318372687
    one_ub = one_mean + (3 * one_sd)
    one_lb = one_mean - (3 * one_sd)

    temp = calculate_horizontal_density(image)
    prediction = 9
    if(temp >= zero_lb and temp < zero_ub): prediction = 0
    if(temp >= one_lb and temp < one_ub): prediction = 1
    return prediction

def make_contingency_table(y, y_hat):
    tp, fn, fp, tn = 0,0,0,0
    for i in range(1, len(y)):
        if(y[i] == 1 and y_hat[i] == 1): tp = tp + 1
        if(y[i] == 0 and y_hat[i] == 1): fp = fp + 1
        if(y[i] == 1 and y_hat[i] == 0): fn = fn + 1
        if(y[i] == 0 and y_hat[i] == 0): tn = tn + 1
    return(tp, fn, fp, tn)

# Enter main section
def main():
    # Open MNIST dataset with pixel files and class files.
    # The data is stored as parquet files
    image_set = pq.read_table('mnist_pixels.parquet')
    image_set = image_set.to_pandas()

    image_class = pq.read_table('mnist_clases.parquet')
    image_class = image_class.to_pandas()
    image_class = pd.to_numeric(image_class['class'])

    # Evaluate average horizontal density for images of 0 and 1
    print("Begin evaluation of images with class 1.")
    results_1 = get_class_average_horizontal_density(image_set, image_class, 1)
    print("Class Average Horizontal Density: ", results_1[0])
    print("Class SD Horizontal Density: ", results_1[1])
    print("Class Occurrences: ", results_1[2], "\n")

    print("Begin evaluation of images with class 0.")
    results_2 = get_class_average_horizontal_density(image_set, image_class, 0)
    print("Class Average Horizontal Density: ", results_2[0])
    print("Class SD Horizontal Density: ", results_2[1])
    print("Class Occurrences: ", results_2[2], "\n")

    # Create a test of all cases with 1 and 0
    pred_value = []
    real_value = []
    for i in range(1, len(image_class)):
        if (image_class.iloc[i] == 1 or image_class.iloc[i] == 0):
            real_value.append(image_class[i])
            temp = transform_clean_format(image_set.iloc[i])
            temp = classifier(temp)
            pred_value.append(temp)

    bar = make_contingency_table(real_value, pred_value)
    dat = {'Positive' : [bar[0], bar[2]],
           'Negative' : [bar[1], bar[3]]}
    df = pd.DataFrame(dat, columns = ['Positive','Negative'], index=['Positive','Negative'])
    print("Contingency Table \n")
    print (df)

if __name__ == "__main__":
    main()