# Find out max and min from the given list.


def get_max(list):
    max = list[0]
    i = 1
    while (i < len(list)):
        if max < list[i]:
            max = list[i]
        i += 1
    return max


def get_min(list):
    min = list[0]
    i = 1
    while i < len(list):
        if min > list[i]:
            min = list[i]
        i += 1
    return min


def get_max_by_other_way(list):
    list.sort()
    return list[len(list) - 1]



my_list = [34, 8, 25, 50, 59, 7, 36, 49, 78, -34, -100]

print('Max: {}'.format(get_max_by_other_way(my_list)))

print('Min: {}'.format(get_min(my_list)))