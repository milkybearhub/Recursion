function recursiveDigitsAdded(digits) {
    let sum = recursiveDigitsAddedHelper(digits, 0)
    if (sum < 10) return recursiveDigitsAddedHelper(sum, 0)

    return sum + recursiveDigitsAdded(sum)
}

function recursiveDigitsAddedHelper(digits, sum) {
    if (digits == 0) return sum

    return recursiveDigitsAddedHelper(Math.trunc(digits / 10), sum + digits % 10)
}

console.log(recursiveDigitsAdded(5))
console.log(recursiveDigitsAdded(8))
console.log(recursiveDigitsAdded(12))
console.log(recursiveDigitsAdded(98))
console.log(recursiveDigitsAdded(3528))
console.log(recursiveDigitsAdded(99999999999884))
console.log(recursiveDigitsAdded(5462))
console.log(recursiveDigitsAdded(45622943))
console.log(recursiveDigitsAdded(9514599))
console.log(recursiveDigitsAdded(8112653648076))
