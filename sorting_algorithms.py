list_sort = [1, 2, 40, 5, 3, -1, 20, 3]
list_sort1 = [1, 50, 5, 56, 89, -5, -1]
sorted_list = []
xdlist = []
sorted_by = 0
i = 0


for i in range(len(list_sort)): #sort numbers by one number
    if list_sort[i] > sorted_by:
        sorted_list = list_sort[i]
        print(sorted_list)


for j in range(len(list_sort1)): #sorting algorithm
    min_index = j
    for k in range(j + 1, len(list_sort1)):
        if list_sort1[min_index] > list_sort1[k]:
            min_index = k

    list_sort1[j], list_sort1[min_index] = list_sort1[min_index], list_sort1[j]

print(list_sort1)
