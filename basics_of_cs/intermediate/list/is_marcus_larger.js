function isMarcusLarger(stringOperand1,stringOperand2) {
  return sumOfCharCode(stringOperand1.toLowerCase()) > sumOfCharCode(stringOperand2.toLowerCase())
}

function sumOfCharCode(string) {
  let total = 0
  for(let i = 0; i < string.length; i++) {
    total += string.codePointAt(i)
  }
  return total
}

console.log(isMarcusLarger("Fantastic","Bridge"))
console.log(isMarcusLarger("Bridge","Fantastic"))
console.log(isMarcusLarger("Appearances may deceive","I think so too"))
