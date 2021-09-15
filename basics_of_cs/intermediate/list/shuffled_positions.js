function shuffledPositions(arr,shuffledArr){
    let hashmap = {}
    for (let i = 0; i < shuffledArr.length; i++) hashmap[shuffledArr[i]] = i

    let result = []
    for (let i = 0; i < arr.length; i++) result.push(hashmap[arr[i]])

    return result
}

console.log(shuffledPositions([2,32,45],[45,32,2]))
console.log(shuffledPositions([10,11,12,13],[12,10,13,11]))
console.log(shuffledPositions([10,11,12,13],[10,11,12,13]))
console.log(shuffledPositions([1350,181,1714,375,1331,943,735],[1714,1331,735,375,1350,181,943]))
