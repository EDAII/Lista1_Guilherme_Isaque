import load_and_prepare_data as ld
import search_methods as sm

data = ld.load_and_prepare_data()
#print(data[0])

#for i in data:
#    print(i)

print("digite o co_cnes do Centro médico")
value=int(input())

result_binary_search_iterative = sm.binary_search(data, value)
result_recursive_binary_search = sm.recursive_binary_search(data, 0, len(data), value)
result_interpolation_search = sm.interpolation_search(data, value)

print(result_recursive_binary_search)
