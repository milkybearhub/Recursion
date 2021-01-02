def reverseString(string):
    if lastIndex(string) < 0: return ""
    return string[lastIndex(string):] + reverseString(string[:lastIndex(string)])

def lastIndex(string):
    return len(string) - 1
