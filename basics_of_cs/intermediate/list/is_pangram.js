function isPangram(string) {
    let hashmap = {}
    let lowerString = string.replace(/ /g, "").toLowerCase()

    for (let i = 0; i < lowerString.length; i++) {
        if (hashmap[lowerString[i]] === undefined) hashmap[lowerString[i]] = 1
        else hashmap[lowerString[i]]++
    }

    return Object.keys(hashmap).length == 26 ? true : false
}

console.log(isPangram("we promptly judged antique ivory buckles for the next prize"))
console.log(isPangram("sheep for a unique zebra when quick red vixens jump over the yacht"))
console.log(isPangram("a quick brown fox jumps over the lazy dog"))
