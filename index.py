import load_and_prepare_data as ld
import interpolation_search as ins

data = ld.load_and_prepare_data()
print(data[0])

#for i in data:
#    print(i)

print("digite o co_cnes do Centro médico")
value=int(input())

result = ins.interpolation_search(data, value)

print(result)
