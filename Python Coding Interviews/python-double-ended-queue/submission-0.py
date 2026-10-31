from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    """
    1 -> Convert list into deque
    2 -> Rotate values to the right by k -> 1,2,3,4,5 k=2 => 4,5,1,2,3
    """

    q = deque(arr)

    for _ in range(k):
        value = q.pop()
        q.appendleft(value)

    return q


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
