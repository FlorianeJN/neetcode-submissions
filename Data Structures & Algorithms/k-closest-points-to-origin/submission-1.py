class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Input -> points where points[i] = [xi,yi], k
        Output -> the k closest points to the origin

        Distance between two points is sqrt((x1 - x2)^2 + (y1 - y2)^2))

        Brute force:    - Calculate the distance for each points and store that in hashmap
                        - Sort my hashmap in ascending order based on distance (value)
                        - Return k first elements in the map
                        Time Complexity -> O(n log n)

        Heap approach:  - Use a max-heap of size k (best k so far)
                        - Go through each point and compute the distance
                        - If distance is best than the top of heap add it (pop from heap if max size)
                        - That way we get rid of worst value and keep adding best values
                        - By the end, the heap will hold the k closest points
                        Time Complexity -> O(n log k)
        """

        heap = []  # Entries are distance, point

        for x, y in points:
            dist = math.sqrt(x * x + y * y)

            if len(heap) < k:
                heapq.heappush_max(heap, (dist, x, y))

            elif dist < heap[0][0]:
                heapq.heapreplace_max(heap, (dist, x, y))

        return [[x, y] for _, x, y in heap]
