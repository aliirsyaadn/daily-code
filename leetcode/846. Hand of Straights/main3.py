from collections import Counter
def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False
    hand.sort()
    cardCount = Counter(hand)
    for card in hand:
        if cardCount[card] == 0:
            continue
        for i in range(groupSize):
            if cardCount[card + i] == 0:
                return False
            cardCount[card + i] -= 1
    return True

print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3)) # true
print(isNStraightHand([1,2,3,4,5], 4)) # false
print(isNStraightHand([1,1,2,2,3,3], 2)) # false
print(isNStraightHand([1,1,2,2,3,3], 3)) # true
print(isNStraightHand([8, 12, 9], 1)) # true
print(isNStraightHand([34,80,89,15,38,69,19,17,97,98,26,77,8,31,79,70,103,3,13,21,81,53,33,14,60,68,33,59,84,23,97,90,76,82,66,83,23,22,16,18,98,25,16,61,84,100,4,68,101,25,23,9,10,55,2,67,39,52,102,99,40,11,83,24,81,53,96,23,13,24,99,67,22,51,31,58,78,88,5,15,24,32,81,91,96,16,54,22,56,69,14,82,32,34,83,24,37,82,54,21], 4)) # true