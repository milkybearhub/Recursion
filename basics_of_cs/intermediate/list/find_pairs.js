function findPairs(numbers) {
    const hashmap = {}
    for (let i = 0; i < numbers.length; i++) {
        hashmap[numbers[i]] == undefined ? hashmap[numbers[i]] = 1 : hashmap[numbers[i]]++
    }

    const keys = Object.keys(hashmap).map(value => Number(value))
    let result = []
    for (let i = 0; i < keys.length; i++) {
        if (hashmap[keys[i]] == 2) result.push(keys[i])
    }

    return result.sort((a, b) => a - b)
}

console.log(findPairs([10,12,13,14,15,16,16,7,7,8]))
console.log(findPairs([1,1]))
console.log(findPairs([1,2]))
console.log(findPairs([1,2,3,4,5,6,6,7,7,8]))
console.log(findPairs([1,3,6,3,1,4,6,4]))
console.log(findPairs([3,3,-1,-1,1,6,6,4,4]))
console.log(findPairs([30,30,30,30,1,600,600,40,40,40]))
