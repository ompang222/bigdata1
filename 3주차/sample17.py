from dask.core import lists_to_tuples

tuple_value = ('1', '2', '3', '4')
list_value = ['5', '6', '7', '8']

print(type(list_value))
print(tuple_value)

tuple_to_list = list(tuple_value)
lists_to_tuple = tuple(list_value)

print(type(lists_to_tuple))
print(type(tuple_to_list))