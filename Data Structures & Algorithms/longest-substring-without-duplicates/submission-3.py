class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        0 1 2 3 4 5
              i   j
        z x y x y z
              _____
        max = 3

        Brute force approach -> Nested loop to detect duplicate characters
        and save longest length : O(n2)

        Sliding window approach -> Use two pointers to create a window 
        and verify duplicates within that window. Adjust window if 
        duplicate character is found : O(n)

        Hashmap needed to store last seen index because everytime we
        adjust the window we go one past the last seen character

        """

        # character -> index
        store = defaultdict(int)
        i , j = 0 , 0
        longest = 0

        while j < len(s):
            ch = s[j]
            if ch in store and store[ch] >= i:
                i = store[ch] + 1
                
            longest = max(longest, j - i + 1)
            store[ch] = j

            j += 1
        return longest


        