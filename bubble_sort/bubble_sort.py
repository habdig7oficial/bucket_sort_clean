def bubble_sort(vec, key = None, reverse = False):

    print(f"\nvec: {vec}")
    if key == None:
        key = vec.copy()
        print(f"\nkey: {key}")
    #print(key)
    
    for i in range(len(vec) - 1):
        for j in range(len(vec) - 1):
            if (key[j] > key[j + 1] and reverse == False) or (key[j] < key[j + 1] and reverse == True):

                aux = key[j]
                key[j] = key[j + 1]
                key[j + 1] = aux
                
                aux = vec[j]
                vec[j] = vec[j + 1]
                vec[j + 1] = aux
                #print(f"key[j]: {key[j]} - {key[j + 1]} - {vec[j]} - {vec[j + 1]}")
                #print(vec)
    return vec
