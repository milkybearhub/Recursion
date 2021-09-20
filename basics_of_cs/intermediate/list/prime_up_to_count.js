function primesUpToNCount(n) {
    // O(n^2)
    // let count = 0
    // for (let i = 0; i < n; i++) if (isPrime(i)) count++
    // return count

    // O(n log logn)
    let list = [...Array(n + 1)].map(n => 0)
    let primes = []
    let i = 2

    while (i < n) {
        if (list[i] == 0) {
            let j = 1

            while (i * j <= n) {
                list[i * j] = 1
                j++
            }
            primes.push(i)
        }
        i++
    }

    return primes.length
}

// function isPrime(number){
//     for (let i = 2; i < number; i++) if (number % i == 0) return false
//     return number > 1
// }

console.log(primesUpToNCount(2))
console.log(primesUpToNCount(3))
console.log(primesUpToNCount(5))
console.log(primesUpToNCount(13))
console.log(primesUpToNCount(18))
console.log(primesUpToNCount(89))
console.log(primesUpToNCount(97))
console.log(primesUpToNCount(100))
console.log(primesUpToNCount(367))
console.log(primesUpToNCount(673))
console.log(primesUpToNCount(1000))
console.log(primesUpToNCount(3406))
console.log(primesUpToNCount(20034))
