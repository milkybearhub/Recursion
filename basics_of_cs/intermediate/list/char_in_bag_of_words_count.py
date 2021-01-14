def charInBagOfWordsCount(bagOfWords,keyCharacter):
    count = 0
    for string in bagOfWords: count += string.count(keyCharacter)
    return count
