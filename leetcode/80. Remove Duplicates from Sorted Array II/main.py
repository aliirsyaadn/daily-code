# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description

def removeDuplicates(nums: list[int]) -> int:
    # Pop all duplicates
    # count = 0
    # i = 0
    # while i < len(nums):
    #     if i > 0 and nums[i] == nums[i-1]:
    #         count += 1
    #         if count > 2:
    #             nums.pop(i)
    #             i -= 1
    #     else:
    #         count = 1
    #     i += 1
    # return len(nums)

    # Two pointers
    slow = 0
    count = 1
    for fast in range(1, len(nums)):
        if nums[fast] == nums[slow]:
            count += 1
            if count <= 2:
                slow += 1
                nums[slow] = nums[fast]
        else:
            count = 1
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


print(removeDuplicates([1,1,1,2,2,3])) # 5
        