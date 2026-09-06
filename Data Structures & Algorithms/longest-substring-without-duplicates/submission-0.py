class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        left = 0

        for right, c in enumerate(s):
            while c in seen: 
                #left ends up equal to right
                # when the previous occurance
                # of the duplicate character
                # is at right-1 index. 
                seen.remove(s[left])
                left += 1

            seen.add(c)

            # +1 in the line below 
            longest = max(longest, right - left +1)

        return longest