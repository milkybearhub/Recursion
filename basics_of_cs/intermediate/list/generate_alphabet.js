function generateAlphabet(firstAlphabet,secondAlphabet) {
    const first = firstAlphabet.toLowerCase()
    const second = secondAlphabet.toLowerCase()
    const diff = second.charCodeAt(0) - first.charCodeAt(0)
    const start = diff > 0 ? first : second
    let result = []

    for (let i = 0; i < Math.abs(diff) + 1; i++) {
        result.push(String.fromCharCode(start.charCodeAt(0) + i))
    }

    return result
}


console.log(generateAlphabet("a","z"))
console.log(generateAlphabet("b","b"))
console.log(generateAlphabet("C","Z"))
console.log(generateAlphabet("M","z"))
console.log(generateAlphabet("z","a"))
