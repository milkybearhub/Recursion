function rotateByTimes(ids, n) {
    let move = n % ids.length
    let popped = []
    for (let i = move; i > 0; i--) { popped = [ids.pop(), ...popped] }
    return [...popped, ...ids]
}

console.log(rotateByTimes([4,23,104,435,5002,3],26))
console.log(rotateByTimes([4,23,104,435,5002,3],0))
console.log(rotateByTimes([2,3],1))
console.log(rotateByTimes([10,12,3,4,5],3))
