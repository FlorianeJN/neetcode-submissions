class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = ["(","{","["]
        pairs = ["()","{}","[]"]

        for ch in s:
            if ch in openings:
                stack.append(ch)
            else:
                if not stack:
                    return False
                last = stack[-1]
                curr = last + ch
                if curr not in pairs:
                    return False
                stack.pop()

        return len(stack) == 0
                
            
        