# https://leetcode.com/problems/base-7/
# 504. Base 7
# Easy
# Topics
# Companies
# Given an integer num, return a string of its base 7 representation.

 

# Example 1:

# Input: num = 100
# Output: "202"
# Example 2:

# Input: num = -7
# Output: "-10"
 

# Constraints:

# -107 <= num <= 107

def convertToBase7(num: int) -> str:
    if num == 0:
        return "0"
    result = ""
    is_negative = num < 0
    num = abs(num)
    while num:
        result = str(num % 7) + result
        num //= 7
    return "-" + result if is_negative else result