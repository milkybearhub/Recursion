def reverseString(string):
    return reverseStringHelper(string[0], 1, string)

# 文字列の切り取りをせずにインデックスをずらす
def reverseStringHelper(reversedString, index, originalString):
    if index >= len(originalString): return reversedString
    return reverseStringHelper(originalString[index] + reversedString, index + 1, originalString)

# Shinyaさんの解答
# https://recursionist.io/dashboard/problems/submissions/32267
