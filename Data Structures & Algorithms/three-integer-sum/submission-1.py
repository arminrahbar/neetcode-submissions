class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array so we can use two pointers
        nums.sort()

        # This will store all valid triplets
        result = []

        # Pick the first number of the triplet
        for i in range(len(nums)):

            # Skip duplicate first numbers
            # Example: if nums[i] and nums[i - 1] are both -1,
            # using both could create duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Start two pointers after i
            left = i + 1
            right = len(nums) - 1

            # Search for two numbers that make the total 0
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # Found a valid triplet
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers inward
                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # If total is too small, move left rightward
                # because we need a larger number
                elif total < 0:
                    left += 1

                # If total is too large, move right leftward
                # because we need a smaller number
                else:
                    right -= 1

        return result