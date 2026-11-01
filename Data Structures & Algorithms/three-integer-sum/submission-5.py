class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        i, j and k are distinct
        nums[i] + nums[j] + nums[k] = 0
        Make sure no duplicates in output
        output can be in any order

        [   [-1,0,1]
            [-1,2,-1]

        ]

        OG arr: [-1, 0, 1, 2, -1, -4]

        Sorted: [-4, -1, -1, 0, 1, 2] 
                 ^
                      ^            ^            

        Brute force approach: Use nested loops to check pairs : O(n3)

        Two pointer approach: Use nested loop to anchor a spot and 
        then two pointer the remaining array.
        Sort the array so that i can move j and k efficiently? The solution is 
        already in O(n2) so sorting is not a big deal!
        For each i, adjust j and k to find triplet.
        How to handle duplicates triplets? Sort and put it in set as tuple?
        
        O(n2) solution
        """

        output = set()
        nums.sort()

        for i,num in enumerate(nums):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum == 0:
                    result = [num,nums[left],nums[right]]
                    result.sort()
                    output.add(tuple(result))
                    left += 1
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
            
        return [list(t) for t in output]
                    

        