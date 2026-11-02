class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []
        nums.sort()

        for i,a in enumerate(nums):

            # no treatment possible
            if a > 0 :
                break

            # Skip duplicates
            if i > 0 and a == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                val = nums[l] + nums[r] + a

                if val < 0:
                    l += 1

                elif val > 0:
                    r -= 1

                else:
                    output.append([a,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    
                    # Skip duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    
        return output

        