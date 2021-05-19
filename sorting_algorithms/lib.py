from time import perf_counter_ns
import random, math, csv

def test_a_sort_function(function, name_of_function):
    """
    benchmarks a function and writes the CSV data in a file
    """
    title = [name_of_function]
    header = ['list_length', 'elapsed_time', 'elapsed_time_log']
    with open('./benchmark_{0}.csv'.format(name_of_function), 'w') as file:
        writer = csv.writer(file)
        writer.writerow(title)
        writer.writerow(header)
        for length in [10, 50, 100, 150, 200, 250, 300, 400, 500, 1000, 2000]:
            print("we test the", name_of_function, "with length", length)
            list = random_list_with_length(length)
            start_time = perf_counter_ns()
            function(list)
            elapsed_time = perf_counter_ns() - start_time
            data = [ length, elapsed_time, math.log(elapsed_time, 10)]
            writer.writerow(data)



def random_list_with_length(limit):
    """
    generates a list of random integers
    """
    list = []
    for _ in range(limit):
        list.append(random.randint(0, limit - 1))
    
    return list

def fusion_sort(list):
    """
    find the min value, append to a list, rince and repeat
    """
    sorted_list = []
    # as many times as there are numbers in the list
    while len(list) > 0:
        # iterate over the list to find the lowest value
        min = list[0]
        for number in list:
            if number < min :
                min = number
        sorted_list.append(min)
        # pop the lowest value and put it into the sorted list
        list.remove(min)
    print("we are done sorting the list")
    

def selection_sort(list):
    """
    with respect to https://en.wikipedia.org/wiki/Selection_sort
    """
    # divide the list in two parts: left is sorted, right is unsorted
    # the diviser_index variable locates where the unsorted start
    for diviser_index in range(0, len(list)):
        # find the smallest element index in the unsorted right
        smaller_number_index = diviser_index
        for i in range(diviser_index, len(list)):
            if list[i] < list[smaller_number_index]:
                smaller_number_index = i
        # swap the first element of the unsorted list with the minimum value
        list[diviser_index], list[smaller_number_index] = list[smaller_number_index], list[diviser_index]
        #print(list)
        # the sorted list got longer by 1
        # so the loop increments the diviser index    

def find_min_find_max(list):
    """
    finds min and max values in a list
    """
    min = list[0]
    max = list[0]
    for number in list:
        if number < min:
            min = number
        if number > max:
            max = number
    print("max number:", max, "min number:", min)
    
    
