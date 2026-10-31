from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    """
    1: Turn list into queue
    2: rotate by k steps -> 1,2,3,4,5 k=2 => 3,4,5,1,2
    """

    q = deque(arr)

    for i in range(k):
        value = q.popleft()
        q.append(value)

    return q




# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
