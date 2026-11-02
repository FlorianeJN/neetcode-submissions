class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        """
        ** A car can not pass another car ahead of it

        Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

        target = 10

            (0,1) (1,2) (4,2) (7,1)
              10   4.5    3     3
              3 fleets

        stack = [10 4.5 3]

        - Create array tuples (position,speed)
        - Sort based on position
        - Use stack to keep track of fleets: if value <= top, 
        get rid of it (dont append) because same fleet.

        Time complexity -> O(n log n) because of sorting
        """
        cars = []
        fleets = []

        for p,s in zip(position,speed):
            cars.append((p,s))

        cars.sort(key=lambda x : x[0], reverse=True) # Sort based on position

        for car in cars:
            pos, spe = car
            distance = target - pos
            time = distance / spe

            if not fleets or time > fleets[-1]:
                fleets.append(time)

        return len(fleets)


        
        