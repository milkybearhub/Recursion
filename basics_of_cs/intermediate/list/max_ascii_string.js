function maxAsciiString(stringList) {
    let sumList = stringList.map(string => sumOfAsciiCode(string.toLowerCase()))
    return sumList.indexOf(Math.max(...sumList))
}

function sumOfAsciiCode(string) {
    let total = 0
    for (let i = 0; i < string.length; i++) { total += string.codePointAt(i) }
    return total
}

console.log(maxAsciiString(["Fantastic","Bridge","Superior","Fantastic","Operator"]))
console.log(maxAsciiString(["HeLlo","HelLo","bridge"]))
console.log(maxAsciiString(["eatDjrPNbj","IehUUSEMVe","hpcbBvlTOc","egvnPZgyCh"]))
console.log(maxAsciiString(["egvnPZgyCh","bridge","Fantastic"]))
