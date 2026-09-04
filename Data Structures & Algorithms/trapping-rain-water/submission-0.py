class Solution:
    def trap(self, height: List[int]) -> int:
        # Mental picture:
        #
        # Imagine these bars as walls of different heights. Water collects in the
        # valleys between taller walls.
        #
        # For any single bar, water can sit above it only if there is a taller
        # wall somewhere on both its left and its right. The water can rise only
        # as high as the shorter of those two walls.
        #
        # We therefore look at the elevation map from both ends at the same time.
        # As we move inward, we remember the tallest wall we have encountered
        # from the left and the tallest wall we have encountered from the right.
        #
        # Whichever of those two walls is shorter controls the current water level.
        # We process that side first because we already know there is a wall on the
        # opposite side that is at least that tall.
        #
        # When we move inward and encounter a new bar:
        #
        #     - If the bar is taller than our previous wall, it becomes the new wall.
        #       There is no water above that bar.
        #
        #     - If the bar is shorter than our wall, it lies inside a valley.
        #       The vertical space between the wall and the bar is filled with water.
        #
        # Example:
        #
        #       wall = 3
        #       bar  = 1
        #
        #       |~~~|
        #       |~~~|   <- 2 units of water above this bar
        #       | | |
        #
        #       water above this bar = 3 - 1 = 2
        #
        # Since every bar has width 1, that vertical difference is exactly the
        # amount of water contributed by that position.
        #
        # We repeat this from both sides and add the water above every bar.

        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        water = 0

        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]

            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water