# Author: Abhash Sharma
# Course: CS 325, Fall 2020
# HW 2, 5a
# implement stooge sort to sort an array/vector of integers
# in descending order

# part of the code that handles opening of data.txt and outputs a file
# is from HW 1.

# CITATION: Wikipedia Article on Stooge Sort Algorithm

def stooge_helper(array, front, end):
    """helper function for stoogesort function"""

    # holds the number of elements in new divided array
    array_elem = end - front + 1

    # when front of array is smaller than last of array
    # elements are swapped
    if array[front] < array[end]:
        temp = array[front]
        array[front] = array[end]
        array[end] = temp
    # when there are more than two elements in array
    if (array_elem) > 2:
        # find the index that represents the 1/3 element of array
        m = int((end - front + 1)/3)
        stooge_helper(array, front, (end - m))
        stooge_helper(array, (front + m), end)
        stooge_helper(array, front, (end - m))
    return array


def stoogesort(array):
    """recursively sorts an array of integers using the stooge sort algorithm"""
    front_elem_index = 0
    last_elem_index = len(array) - 1
    # call to helper function
    return stooge_helper(array, front_elem_index, last_elem_index)

# import file "data.txt"
with open('data.txt', 'r') as infile:
    # iterate through each line
    for line in infile:
        # remove '/n' from each line
        clean_line = line.strip()
        # turn array of strings into array of integers
        un_str_array = clean_line.split(' ')
        un_int_array = []
        for i in un_str_array:
            un_int_array.append(int(i))
        # remove the first element from unsorted array
        # this is according to assignment requirements
        unsorted_array = un_int_array[1:]
        # sort each array
        sorted_array = stoogesort(unsorted_array)
        # write each line as string to a file
        with open('stooge.out', 'a') as outfile:
            for k in range(0, len(sorted_array)):
                outfile.write(str(sorted_array[k]) + str(' '))
            outfile.write('\n')
            outfile.close()