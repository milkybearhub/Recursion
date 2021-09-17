function intersectionOfArraysRepeats(intList1,intList2){
    let hashmap = {}
    for (let i = 0; i < intList2.length; i++) {
        hashmap[intList2[i]] == undefined ? hashmap[intList2[i]] = 1 : hashmap[intList2[i]]++
    }

    const sortedIntList1 = intList1.sort((a, b) => a - b)
    let result = []

    for (let i = 0; i < sortedIntList1.length; i++) {
        if (hashmap[sortedIntList1[i]] == undefined || hashmap[sortedIntList1[i]] == 0) continue

        result.push(sortedIntList1[i])
        hashmap[sortedIntList1[i]]--
    }

    return result
}

console.log(intersectionOfArraysRepeats([3,2,1],[3,2,1]))
console.log(intersectionOfArraysRepeats([1,1,1],[1,2,3,2,1]))
console.log(intersectionOfArraysRepeats([3,2,2,2,1,10,10],[3,2,10,10,10]))
console.log(intersectionOfArraysRepeats([2,19,11,2,6,8],[10,23,5,8,19]))
console.log(intersectionOfArraysRepeats([4,22,100,88,6,8],[1,2,3]))
console.log(intersectionOfArraysRepeats([-1,-2,-1,-1],[-1,-1,-2,-2]))
console.log(intersectionOfArraysRepeats([1,2,2,1],[2,2,2,1]))
console.log(intersectionOfArraysRepeats([4,9,5],[9,4,9,8,4]))
