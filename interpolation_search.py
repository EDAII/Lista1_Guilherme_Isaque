
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
