function twosComplement(bits) {
    return plusOne(oneComplement(bits))
}

function oneComplement(bits) {
    let result = ""
    for(let i = 0; i < bits.length; i++) {
        result += bits[i] === "0" ? "1" : "0"
    }
    return result
}

function plusOne(bits) {
    let count = 0
    for(let i = bits.length -1; i >= 0; i--) {
        if (bits[i] === "0") {
            let zeros = count === 0 ? "" : "0".repeat(count)
            return bits.substring(0, i) + "1" + zeros
        }
        count += 1
    }
    // 桁が増える場合
    return "1" + "0".repeat(count)
}

console.log(twosComplement("00011100"))
console.log(twosComplement("10010"))
console.log(twosComplement("001001"))
console.log(twosComplement("0111010"))
console.log(twosComplement("1"))
console.log(twosComplement("0"))
console.log(twosComplement("000"))
