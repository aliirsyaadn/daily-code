# https://leetcode.com/problems/hand-of-straights/description/
def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False
    hand.sort()
    
    double_hand = []
    groupCount = len(hand) // groupSize
    i = 0
    for _ in range(groupCount):
        i_double_hand = 0
        currentVal = None
        if len(double_hand) != 0 :
            currentVal = double_hand[i_double_hand]
            double_hand.remove(double_hand[i_double_hand])
        else:
            currentVal = hand[i]
            i += 1

        currentGroupSize = 1
        skipDoubleHand = False
        while i_double_hand < len(double_hand) or i < len(hand):
            if currentGroupSize == groupSize:
                break
            if i_double_hand < len(double_hand) and not skipDoubleHand :
                if currentVal + 1 == double_hand[i_double_hand]:
                    currentVal = double_hand[i_double_hand]
                    double_hand.remove(double_hand[i_double_hand])
                    currentGroupSize += 1
                elif currentVal + 1 < double_hand[i_double_hand]:
                    skipDoubleHand = True
                else:
                    i_double_hand += 1
            elif i < len(hand) :
                if currentVal + 1 == hand[i]:
                    currentVal = hand[i]
                    currentGroupSize += 1
                    i += 1
                elif currentVal == hand[i]:
                    double_hand.append(hand[i])
                    i += 1
                else :
                    return False
            else:
                return False
            
        if currentGroupSize != groupSize:
            return False
            
    
    return True


print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3)) # true
print(isNStraightHand([1,2,3,4,5], 4)) # false
print(isNStraightHand([1,1,2,2,3,3], 2)) # false
print(isNStraightHand([1,1,2,2,3,3], 3)) # true
print(isNStraightHand([8, 12, 9], 1)) # true
print(isNStraightHand([34,80,89,15,38,69,19,17,97,98,26,77,8,31,79,70,103,3,13,21,81,53,33,14,60,68,33,59,84,23,97,90,76,82,66,83,23,22,16,18,98,25,16,61,84,100,4,68,101,25,23,9,10,55,2,67,39,52,102,99,40,11,83,24,81,53,96,23,13,24,99,67,22,51,31,58,78,88,5,15,24,32,81,91,96,16,54,22,56,69,14,82,32,34,83,24,37,82,54,21], 4)) # true
