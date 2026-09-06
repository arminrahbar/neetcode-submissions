class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Mental picture:
        #
        # Keep a window between left and right.
        #
        # Inside that window, find the character that appears the most.
        # We would keep all copies of that character and replace every
        # other character in the window.
        #
        # Example:
        #
        #     window = "AABA"
        #
        #     A appears 3 times
        #     window size = 4
        #
        #     replacements needed = 4 - 3 = 1
        #
        # If replacements_needed <= k, the whole window can be turned
        # into one repeated character, so the window is valid.
        #
        # If replacements_needed > k, we need too many replacements.
        # Shrink the window from the left until it becomes valid again.
        #
        # As right moves through the string, keep track of the longest
        # valid window we have seen.

        count = {}
        left = 0
        max_frequency = 0
        longest = 0

        for right, char in enumerate(s):
            # Add the new character to the current window.
            count[char] = count.get(char, 0) + 1

            # Track how many times the most common character
            # has appeared inside the current window.
            max_frequency = max(max_frequency, count[char])

            # Number of characters that must be changed so that
            # every character in the window becomes the most common one.
            window_size = right - left + 1
            replacements_needed = window_size - max_frequency

            # If we need more than k replacements, the window is invalid.
            # Remove characters from the left until the window fits again.
            while replacements_needed > k:
                count[s[left]] -= 1
                left += 1

                window_size = right - left + 1
                replacements_needed = window_size - max_frequency

            # The current window can be turned into one repeated character
            # using at most k replacements.
            longest = max(longest, window_size)

        return longest