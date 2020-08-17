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

# SCRATCH PAD... PLEASE ELIMINATE IN FINAL PROGRAM

def transform_to_image_matrix(dataframe_iloc):
    """Get an image class block and return 28 x 28 matrix for analysis

    :parameter
    dataframe_iloc

    :return
    temp
    """
    temp = dataframe_iloc.to_list()
    temp: ndarray = np.reshape(temp, (28, 28))
    return temp

def print_horizontal_average(some_image_matrix):
    """Print the average pixel value for the 28 rows in an image matrix
    :parameter
    some_image_matrix

    :return

    """
    row_mean_counter = []
    i = 0
    for rows in some_image_matrix:
        print("mean for row", i, " is ", np.mean(rows))
        row_mean_counter.append(np.mean(rows))
        i = i + 1
    print(">>> FINAL MEAN: ", np.mean(row_mean_counter))
    return np.mean(row_mean_counter)




def calculate_horizontal_average(some_image_matrix):
    """Calculate the average pixel value for the 28 rows in an image matrix
    :parameter
    some_image_matrix

    :return

    """
    row_mean_counter = []
    for rows in some_image_matrix:
        row_mean_counter.append(np.mean(rows))
    return np.mean(row_mean_counter)

def test_image(image, real_class, image_id):
    """Automated test of images for classification
    :parameter image
    :parameter real_class
    :parameter image_id

    :return

    """
    print("automated test for image in location: ", image_id)
    print("-----------------------------------------")
    print("value of real image is: ", real_class)
    test_image = transform_to_image_matrix(image)

    print("average row value for 28 rows is: ", calculate_horizontal_average(test_image))



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

if __name__ == "__main__":
    main()