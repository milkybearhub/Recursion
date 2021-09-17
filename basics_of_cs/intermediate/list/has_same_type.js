function hasSameType(user1, user2) {
    const hashmap1 = createHashMap(user1, user2)
    const hashmap2 = createHashMap(user2, user1)

    if (Object.keys(hashmap1).length != Object.keys(hashmap2).length) return false

    for (let i = 0; i < user1.length; i++) {
        if (user1[i] != hashmap2[hashmap1[user1[i]]]) return false
    }

    return true
}

function createHashMap(string1, string2) {
    let hashmap = {}
    for (let i = 0; i < string1.length; i ++) hashmap[string1[i]] = string2[i]
    return hashmap
}

console.log(hasSameType("aabb","yyza"))
console.log(hasSameType("aappl","bbtte"))
console.log(hasSameType("aappl","bbttb"))
console.log(hasSameType("aabb","abab"))
console.log(hasSameType("aappl","bktte"))
console.log(hasSameType("aaapppl","bbbttke"))
console.log(hasSameType("abcd","tso"))
console.log(hasSameType("abcd","jklm"))
console.log(hasSameType("aaabbccdddaa","jjjddkkpppjj"))
console.log(hasSameType("aaabbccdddaa","jjjddkkpppjd"))
