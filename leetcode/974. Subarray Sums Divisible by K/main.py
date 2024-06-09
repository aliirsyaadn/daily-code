# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
# 974. Subarray Sums Divisible by K
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:

# Input: nums = [5], k = 9
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104``
# 2 <= k <= 104

def subarraysDivByK(nums: list[int], k: int) -> int:
    n = len(nums)
    if k == 0:
        for i in range(1, n):
            if nums[i] == 0 and nums[i - 1] == 0:
                return 1
        return 0
    if k < 0:
        k = -k
    prefix = [0] * n
    prefix[0] = nums[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + nums[i]
    remainders = {}
    remainders[0] = 1
    for i in range(n):
        remainder = prefix[i] % k
        if remainder in remainders:
            remainders[remainder] += 1
        else:
            remainders[remainder] = 1
    ans = 0
    for remainder in remainders:
        ans += remainders[remainder] * (remainders[remainder] - 1) // 2
    return ans


print(subarraysDivByK([4,5,0,-2,-3,1], 5))
print(subarraysDivByK([5], 9))
print(subarraysDivByK([-5], 5))