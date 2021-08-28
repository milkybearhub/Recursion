function decimalToHexadecimal(decNumber){
    // Best Answer
    let hexaDecimal = '0123456789ABCDEF'
    let result = ''
    let currentHexa

    while (decNumber > 0) {
        currentHexa = decNumber % 16
        result = hexaDecimal[currentHexa] + result
        decNumber = Math.floor(decNumber / 16)
    }

    return result

    // let result = ''

    // while (decNumber / 16 > 0) {
    //     currentHexa = replace(decNumber % 16)
    //     decNumber = Math.floor(decNumber / 16)
    //     result = currentHexa.toString() + result
    // }

    // return result
}

// function replace(decNumber) {
//     if (decNumber < 10) { return decNumber }

//     switch (decNumber) {
//         case 10:
//             return 'A'
//         case 11:
//             return 'B'
//         case 12:
//             return 'C'
//         case 13:
//             return 'D'
//         case 14:
//             return 'E'
//         case 15:
//             return 'F'
//     }
// }

console.log(decimalToHexadecimal(532454))
console.log(decimalToHexadecimal(90304))
console.log(decimalToHexadecimal(28394))
console.log(decimalToHexadecimal(15))
console.log(decimalToHexadecimal(74))
