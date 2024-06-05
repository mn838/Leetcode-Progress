class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return_list = [0] * 2 * len(nums)   # Initialize a list of size 2 * len(nums) with 0s

        for i in range( len( nums ) ):
            return_list[i] = nums[i]    # Copy the elements of nums to the first half of return_list
            return_list[i + len(nums)] = nums[i]    # Copy the elements of nums to the second half of return_list
        
        return return_list