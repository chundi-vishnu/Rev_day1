def sort_tuples(data): 
    return sorted(data, key=lambda x: (-sum(x), x[0])) 
data = [(3, 5), (1, 8), (4, 4), (2, 6)] 
sorted_data = sort_tuples(data) 
print(sorted_data)