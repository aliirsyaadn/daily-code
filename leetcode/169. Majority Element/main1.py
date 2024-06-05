# https://leetcode.com/problems/majority-element/description

def majorityElement(nums: list[int]) -> int:
    currentWinner = None
    mapCount = {}
    highestCount = 0
    for num in nums:
        if mapCount.get(num):
            mapCount[num] += 1
        else :
            mapCount[num] = 1
        if highestCount < mapCount[num]:
            currentWinner = num
            highestCount = mapCount[num]

    return currentWinner


print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))