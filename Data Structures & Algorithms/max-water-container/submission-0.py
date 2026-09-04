class Solution:
    def maxArea(self, heights: List[int]) -> int:
                # Start with one pointer at the far left
        # and one pointer at the far right.
        left = 0
        right = len(heights) - 1

        # Store the best area found so far.
        max_water = 0

        # Keep moving the pointers toward each other.
        while left < right:
            # Width is the distance between the two bars.
            width = right - left

            # The water height is limited by the shorter bar.
            # Even if one bar is very tall, water spills over the shorter side.
            current_height = min(heights[left], heights[right])

            # Calculate the area formed by these two bars.
            area = width * current_height

            # Update the best answer if this area is larger.
            max_water = max(max_water, area)

            # Move the pointer at the shorter bar.
            # Why? The shorter bar limits the water height.
            # Moving the taller bar cannot help if the shorter bar stays the same.
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water