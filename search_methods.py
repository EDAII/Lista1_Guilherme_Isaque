# Busca sequencial
def sequential_search(data, value):
    size = len(data)
    for index in range(size):
        if data[index][0] == value:
            return index

    return -1

# Cria lista de index
def create_index_list(data, index_size):
    indexed_list = []

    for value in range(0, len(data), index_size):
        indexed_list.append(value)

    return indexed_list

# Busca sequencial indexada
def indexed_sequential_search(data, indexed_list, value):
    if value < data[0][0]:
        print("Valor não encontrado")
        return -1
        exit(0)
    else:
        for indexed in range(len(indexed_list)):
            if data[indexed_list[indexed]][0] == value:
                return indexed_list[indexed]
            elif data[indexed_list[indexed]][0] > value:
                for index in range(indexed_list[indexed - 1], indexed_list[indexed]):
                    if data[index][0] == value:
                        return index
                    elif data[index][0] > value:
                        return -1

# Busca por interpolação
def interpolation_search(data, value):
    start = 0
    end = len(data)-1
    flag = 0
    while(start <= end and value >= data[start][0] and value <= data[end][0]):
        if(start == end):
            if data[start][0] == value:
                # print(start)
                return start
                flag = 1
            else:
                print("-1")
        random = start + \
            int((
                (float(end-start)/(data[end][0]-data[start][0]))*(value-data[start][0])))
        if data[random][0] == value:
            # print(random)
            return random
            flag = 1
        if data[random][0] < value:
            start = random+1
        else:
            end = random-1
    if(flag == 0):
        print("-1 Flag = 0")


# busca binária iterativa
def binary_search(data, value):
    left, right = 0, len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        if data[middle][0] == value:
            return middle
        elif data[middle][0] > value:
            right = middle - 1
        else:  # data[middle] < value
            left = middle + 1
    return -1

# busca binária recursiva
def recursive_binary_search(data, left, right, value):
    if right < left:
        return -1
    middle = (left + right) // 2
    if data[middle][0] == value:
        return middle
    elif data[middle][0] > value:
        return recursive_binary_search(data, left, middle - 1, value)
    else:  # data[middle][0] < value
        return recursive_binary_search(data, middle + 1, right, value)
