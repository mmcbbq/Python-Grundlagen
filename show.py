my_list = [50, 50.55, 'string', True, [1, 2, 3]]
my_list_copy = my_list[:]

# my_list_copy = my_list
print(my_list)
print(my_list_copy, 'copy')
my_list[-1].pop()
print(my_list)
print(my_list_copy, 'copy')
# print('#########################')
# my_list = [50, 50.55, 'string', True]
#
# my_list_copy = my_list.copy()
# my_list.pop()
# print(my_list)
# print(my_list_copy, 'copy')
#
# my_list_copy = list(my_list)  # -> das gleiche Ergebnis wie mit Copy
