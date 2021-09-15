function fireEmployees(employees, unemployed) {
    let hashmap = {}
    for (let i = 0; i < unemployed.length; i++) hashmap[unemployed[i]] = unemployed[i]

    let result = []
    for (let i = 0; i < employees.length; i++) {
        if (hashmap[employees[i]] === undefined) result.push(employees[i])
    }

    return result
}

console.log(fireEmployees(["Steve","David","Mike","Donald","Lake","Julian"],["Donald","Lake"]))
console.log(fireEmployees(["Donald","Lake"],["Donald","Lake"]))
console.log(fireEmployees(["Steve","David","Mike","Donald","Lake","Julian"],[]))
console.log(fireEmployees(["Mike","Steve","David","Mike","Donald","Lake","Julian"],["Mike"]))
