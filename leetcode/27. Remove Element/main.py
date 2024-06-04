# https://leetcode.com/problems/remove-element/description/

def removeElement(self, nums: list[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    
    return i