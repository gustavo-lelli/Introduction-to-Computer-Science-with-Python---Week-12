def ordena(vector):
    for i in range(len(vector)): 
        min_idx = i 
        for j in range(i+1, len(vector)): 
            if vector[min_idx] > vector[j]: 
                min_idx = j 
        vector[i], vector[min_idx] = vector[min_idx], vector[i] 

    return vector
