function missingItems(listA, listB){
    let hashmap = {}
    for (let i = 0; i < listB.length; i++) {
        if (hashmap[listB[i]] === undefined) hashmap[listB[i]] = listB[i]
    }

    let result = []
    for (let i = 0; i < listA.length; i ++) {
        if (hashmap[listA[i]] === undefined) result.push(listA[i])
    }

    return result
}

console.log(missingItems([1,2,3,4,5,6,7,8],[1,3,5]))
console.log(missingItems([1,2,3,4,5],[1,2]))
console.log(missingItems([1,1],[2,2]))
console.log(missingItems([9,8,7,6,5],[1,2]))
console.log(missingItems([8,3,45,67,23,9,3],[3]))
