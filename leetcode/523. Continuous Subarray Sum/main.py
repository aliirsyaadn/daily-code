# https://leetcode.com/problems/continuous-subarray-sum/description/
# 523. Continuous Subarray Sum
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= sum(nums[i]) <= 231 - 1
# 1 <= k <= 231 - 1

def checkSubarraySum(nums: list[int], k: int) -> bool:
    n = len(nums)
    if n < 2:
        return False
    if k == 0:
        for i in range(1, n):
            if nums[i] == 0 and nums[i - 1] == 0:
                return True
        return False
    if k < 0:
        k = -k
    prefix = [0] * n
    prefix[0] = nums[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + nums[i]
    remainders = {}
    remainders[0] = -1
    for i in range(n):
        remainder = prefix[i] % k
        if remainder in remainders:
            if i - remainders[remainder] >= 2:
                return True
        else:
            remainders[remainder] = i
    return False