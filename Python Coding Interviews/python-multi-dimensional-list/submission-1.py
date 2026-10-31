from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    maximums = []

    for arr in nested_arr:
        current_max = float("-inf")
        for value in arr:
            current_max = max(value,current_max)
        maximums.append(current_max)
    
    return maximums



# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
