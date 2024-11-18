

def bucket_sort(array: list[float]):
    buckets = [[] for i in range(len(array))]
    print(f"Balde Vazio: {buckets}\n")
    i = 0
    while i < len(array):
        index = int(array[i] * len(array))
        buckets[index].append(array[i])
        print(f"i: {i} nº do balde: {index} valor inserido: {array[i]}\n{buckets}\n")
        i += 1
    
    return buckets

def bucket_sort_built_in(array: list[float]):
    buckets = bucket_sort(array)
    i = 0
    while i < len(buckets):
        buckets[i].sort()
        i += 1
    flatten = [j for i in buckets for j in i]
    return flatten

from bubble_sort.bubble_sort import bubble_sort as py_bubble

def bucket_sort_bubble(array: list[float]):
    buckets = bucket_sort(array)
    i = 0
    while i < len(buckets):
        buckets[i] = py_bubble(buckets[i])
        i += 1
    flatten = [j for i in buckets for j in i]
    return flatten



from c_bubble_sort.ordination import *

def bucket_sort_c_bubble(array: list[float]):
    buckets = bucket_sort(array)
    i = 0
    result = []
    while i < len(buckets):
        c_arr = to_c_array(buckets[i])
        res = bubble_sort(c_arr, len(buckets[i]))

        j = 0 
        while j < len(buckets[i]):
            result.append(res[j])
            j += 1
        i += 1
    return result