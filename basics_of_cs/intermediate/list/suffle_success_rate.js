function shuffleSuccessRate(arr, shuffledArr) {
    let hashmap = {}
    for (i = 0; i < arr.length; i++) {
        hashmap[arr[i]] = [arr.indexOf(arr[i]), shuffledArr.indexOf(arr[i])]
    }

    let shuffledCount = 0
    for (i = 0; i < arr.length; i++) {
        if (hashmap[arr[i]][0] != hashmap[arr[i]][1]) shuffledCount++
    }

    return Math.trunc((shuffledCount * 100) / arr.length)
}

console.log(shuffleSuccessRate([2,32,45],[45,32,2]))
console.log(shuffleSuccessRate([2,32,45],[45,2,32]))
console.log(shuffleSuccessRate([2,32,45],[2,32,45]))
console.log(shuffleSuccessRate([2,32,45,67],[2,32,67,45]))
console.log(shuffleSuccessRate([2,32,45,67,89],[2,89,67,45,32]))
console.log(shuffleSuccessRate([119,726,398,187,943,486,728,305,968,754,650,536,969,305,111,225,708,806,40,969],[708,969,111,398,754,726,536,943,486,305,969,40,650,806,187,225,968,119,728,305]) )