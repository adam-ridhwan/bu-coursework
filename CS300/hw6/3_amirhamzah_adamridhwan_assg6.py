import copy

def extend_partitions(some_partitions, a_new_element):
    '''
    Preconditions:
    1. some_partitions consists of partition of a set S (which need
    not be specified!) in the form of a list of lists of the set's elements.
    Example: S = {0, 11}, some_partitions = [[[0, 11]], [[0], [11]]]
    2. a_new_element does not occur in some_partitions

    Returns: returned_partitions = all partitions of (S union {a_new_element})

    Example: for S = {0, 11} and a_new_element = 22, this returns the following
    list (containing 5 elements): [[[0, 11, 22]], [[0, 22], [11]],
    [[0], [11, 22]], [[0, 11], [22]], [[0], [11], [22]]]
    '''
    returned_partitions = []

    # (Excluding [a_new_element]): returned_partition includes all partitions
    # of (S union {a_new_element}) that don't contain the list [a_new_element]

    # Example: For S = {0, 11} and a_new_element = 22, returned_partitions would include
    # [[0, 11, 22]], [[0, 22], [11]], [[0], [11, 22]], and [[[0], [11]], 22]]]
    # (notice that none of these partitions contains [22])

    for _partition in some_partitions:  # e.g., _partition = [[0], [11]]
        for i in range(len(_partition)):  # e.g., i points to [0]
            new_partition = copy.deepcopy(_partition)
            new_partition[i].append(a_new_element)  # e.g., get [[0, 22], [11]]
            returned_partitions.append(new_partition)

    # (Including [a_new_element]): returned_partition includes all partitions
    # of S union {a_new_element} that contain [a_new_element]

    # e.g., For the example above, returned_partition includes
    # [[0, 11], [22]] and [[0], [11], [22]]]

    for _partition in some_partitions:  # e.g., [[0, 11]]
        appended_partition = copy.deepcopy(_partition)
        appended_partition.append([a_new_element])
        returned_partitions.append(appended_partition)
        # e.g., append [[0, 11], [22]] in the example

    return returned_partitions


def all_partitions_of(a_list):
    '''
    Precondition: a_list is any list

    Returns returned_partitions = a list of all partitions of a_list}

    Example: for a_list = [0, 11, 22], this function returns
    [[[0, 11, 22]], [[0, 22], [11]], [[0], [11, 22]], [[0, 11], [22]],
     [[0], [11], [22]]]
    '''

    if len(a_list) < 2:
        return [[a_list]]

    returned_partitions = [[[a_list[0]]]]
   
    counter = 1
    while counter < len(a_list): 
        returned_partitions = extend_partitions(returned_partitions, a_list[-1])  
        return returned_partitions


print("[[[]]]<-->" + str(all_partitions_of([])) + '\n')  # one list--consisting of []
print("[[[333]]]<-->" + str(all_partitions_of([333])) + '\n')

print('all_partitions_of([0,22]):')
print(all_partitions_of([0,22]))
print("[[[0, 22]], [[0], [22]]]\n")

print('all_partitions_of([0,11,22]):')
print(all_partitions_of([0,11,22]))
print("[[[0, 22], [11]], [[0], [11, 22]], [[0, 11, 22]], [[0], [11], [22]], [[0, 11], [22]]]\n")

print('all_partitions_of([0,11,22,33]):')
print(all_partitions_of([0,11,22,33]))
print()

print('all_partitions_of([7,8,1,3,5]):')
print(all_partitions_of([7,8,1,3,5]))
