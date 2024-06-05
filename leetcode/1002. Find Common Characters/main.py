# https://leetcode.com/problems/find-common-characters/description
def commonChars(words: list[str]) -> list[str]:
    basedWord = words.pop(0)
    mapWord = {}
    for c in basedWord:
        if mapWord.get(c):
            mapWord[c] += 1
        else :
            mapWord[c] = 1
            
    for word in words:
        currentMapWord = {}
        for c in word:
            if mapWord.get(c):
                if currentMapWord.get(c):
                    if currentMapWord[c] < mapWord[c]:
                        currentMapWord[c] += 1
                else:
                    currentMapWord[c] = 1
        mapWord = currentMapWord
    
    result = []
    for k, v in mapWord.items():
        result += [k]*v
    return result


words = ["bella","label","roller"]
print(commonChars(words))


