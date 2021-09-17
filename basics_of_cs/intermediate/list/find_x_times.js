function findXTimes(teams){
    let hashmap = {}
    for (let i = 0; i < teams.length; i++) {
        hashmap[teams[i]] == undefined ? hashmap[teams[i]] = 1 : hashmap[teams[i]]++
    }

    const keys = Object.keys(hashmap)
    for (let i = 0; i < keys.length; i++) {
        if (hashmap[keys[i]] != hashmap[keys[0]]) return false
    }

    return true
}

console.log(findXTimes("bacddc"))
console.log(findXTimes("babcddc"))
console.log(findXTimes("babacddc") )
console.log(findXTimes("aaabbbcccddd"))
console.log(findXTimes("aaabbccdd"))
console.log(findXTimes("zadbchvwxbwhdxvcza"))
console.log(findXTimes("zadbchvwxbwhdxvczb"))
console.log(findXTimes("zab"))
console.log(findXTimes("z"))
