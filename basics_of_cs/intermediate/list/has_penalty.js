function hasPenalty(records){
    for (let i = 0; i < records.length - 1; i++) {
        if (records[i] > records[i + 1]) return true
    }
    return false
}

console.log(hasPenalty([1,2,3,4]))
console.log(hasPenalty([4,3,2,1]))
console.log(hasPenalty([4,3,3,2,1]))
console.log(hasPenalty([150,130,130,82,51]))
console.log(hasPenalty([100,200,200,200,300,400]))