import load_and_prepare_data as ld
import search_methods as sm

data = ld.load_and_prepare_data()
# print(data)
for i in data:
    print(i)

print("digite o co_cnes do Centro médico")
value = int(input())

result_binary_search_iterative = sm.binary_search(data, value)
result_recursive_binary_search = sm.recursive_binary_search(
    data, 0, len(data), value)
result_interpolation_search = sm.interpolation_search(data, value)
result_sequential_search = sm.sequential_search(data, value)
index_list = sm.create_index_list(data, 1000)
result_indexed_sequential_search = sm.indexed_sequential_search(
    data, index_list, value)

print("recursive_binary_search", result_recursive_binary_search)
print("binary_search", result_recursive_binary_search)
print("interpolation_search", result_interpolation_search)
print("sequential_search", result_sequential_search)
print("indexed_sequential_search", result_recursive_binary_search)
