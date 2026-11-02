class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Use stack to store [value,index] for those waiting to be treated
        For every num check if last of stack can be treated. Stop when we can't
        or stack is empty

        Monotonic stack -> O(n) approach
        """
        stack = []
        output = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            if not stack:
                stack.append((t,i))

            else:
                while stack and t > stack[-1][0]:
                    _, top_index = stack.pop()
                    output[top_index] = i - top_index
                stack.append((t,i))
        
        return output
        


        