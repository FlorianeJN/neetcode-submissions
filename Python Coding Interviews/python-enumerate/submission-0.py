from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for index,value in enumerate(nums):
        if value == 7:
            return index
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    idx_first_occurence = None

    for idx,value in enumerate(nums):
        if value == 7 and idx_first_occurence is None:
            idx_first_occurence = idx
        elif value == 7 :
            return idx - idx_first_occurence
    
    return -1



# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
