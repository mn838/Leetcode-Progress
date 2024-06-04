class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}   #  initializing the hashset

        for num in nums:   #  iterate through the list of nums
            if num in seen and seen[num] >= 1:   # if the number is in the hashset and the count of the number is greater than oe equal to 1
                return True    #  return true
            seen[num] = seen.get(num, 0) + 1   # else add the number to the hashset and increment the count of the number
        return False   # return false if no duplicates were found
