def busca(vector, element):
    for i in range(len(vector)):
        if vector[i] == element:
            return i

    return False
