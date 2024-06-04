def find_common_chars(word_list):
    # implement here
    char_set = set(word_list[0])
    result = []
    for char in char_set:
        list_count = []
        for word in word_list:
            list_count.append(word.count(char))
        min_count = min(list_count)
        for i in range(min_count):
            result.append(char)
    return result
    
print(find_common_chars(["bella", "label", "roller"]))
print(find_common_chars(["cool","lock","cook"]))
print(find_common_chars(["bela","label","roller","lullaby"]))


