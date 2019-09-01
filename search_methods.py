
def interpolation_search(data, value):
    start=0
    end=len(data)-1
    flag=0

    while(start<=end and value>=data[start][0] and value<=data[end][0]):
        if(start==end):
            if data[start][0] == value:
                #print(start)
                return start
                flag=1
            else:
                print("-1")
        random = start + int(((float(end-start)/(data[end][0]-data[start][0]))*(value-data[start][0])))
        if data[random][0]==value:
            #print(random)
            return random
            flag=1
        if data[random][0]<value:
            start= random+1
        else:
            end= random-1
    if(flag==0):
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
        else: # data[middle] < value
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
    else: # data[middle][0] < value
        return recursive_binary_search(data, middle + 1, right, value)
