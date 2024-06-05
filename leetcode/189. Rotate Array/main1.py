# https://leetcode.com/problems/rotate-array/description

def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    temp = nums[:-k]
    nums[:-k] = nums[-k:]
    nums[-k:] = temp

lst = [1,2,3,4,5,6,7]
rotate(lst, 3)
print(lst)