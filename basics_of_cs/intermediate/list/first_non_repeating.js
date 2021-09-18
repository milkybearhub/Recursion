function firstNonRepeating(s) {
    let hashmap = {}
    for (let i = 0; i < s.length; i++) {
        hashmap[s[i]] == undefined ? hashmap[s[i]] = 1 : hashmap[s[i]]++
    }

    for (const key in hashmap) {
        if (hashmap[key] == 1) return s.indexOf(key)
    }

    return -1
}

console.log(firstNonRepeating("aabbcdddeffg"))
console.log(firstNonRepeating("abcdabcdf"))
console.log(firstNonRepeating("abcddaebcdf"))
console.log(firstNonRepeating("aabbbccdd") )
console.log(firstNonRepeating("ddecdfgf"))
console.log(firstNonRepeating("abcdeeff"))
console.log(firstNonRepeating("zzcbdefghafhgbbcd"))
