function winnerPairOfCards(player1, player2){
    // 処理の都合上10を1と読み替える
    const cards = ["A", "K", "Q", "J", 1, 9, 8, 7 ,6, 5, 4 ,3 ,2]
    const hashmap1 = createHashMap(player1, cards)
    const hashmap2 = createHashMap(player2, cards)

    let winner = "draw"
    let max = 0
    for (let i = 0; i < cards.length; i++) {
        if (hashmap1[cards[i]] > hashmap2[cards[i]]) {
            if (hashmap1[cards[i]] > max) {
                winner = "player1"
                max = hashmap1[cards[i]]
            }
        } else if (hashmap1[cards[i]] < hashmap2[cards[i]]) {
            if (hashmap2[cards[i]] > max) {
                winner = "player2"
                max = hashmap2[cards[i]]
            }
        }
    }

    return winner
}

function createHashMap(player, cards) {
    let hashmap = {}
    for (let i = 0; i < cards.length; i++) hashmap[cards[i]] = 0
    for (let i = 0; i < player.length; i++) hashmap[player[i][1]]++
    return hashmap
}

console.log(winnerPairOfCards(["♣4","♥7","♥7","♠Q","♣J"],["♥10","♥6","♣K","♠Q","♦2"]))
console.log(winnerPairOfCards(["♣4","♥7","♥7","♠Q","♣J"],["♥7","♥7","♣K","♠Q","♦2"]))
console.log(winnerPairOfCards(["♣A","♥2","♥3","♠4","♣5"],["♥A","♥2","♣3","♠4","♦5"]))
console.log(winnerPairOfCards(["♣A","♥A","♥A","♠4","♣5"],["♥A","♥A","♣A","♠4","♦5"]))
console.log(winnerPairOfCards(["♣9","♥8","♥7","♠4","♣5"],["♥10","♥8","♣7","♠4","♦5"]))
console.log(winnerPairOfCards(["♣A","♥A","♥2","♠3","♣4"],["♥6","♥6","♣Q","♠Q","♦8"]))
console.log(winnerPairOfCards(["♣A","♥A","♥A","♠3","♣4"],["♥6","♥6","♣Q","♠Q","♦Q"]))
console.log(winnerPairOfCards(["♣K","♥K","♥K","♠A","♣A"],["♥6","♥6","♣Q","♠Q","♦Q"]))
console.log(winnerPairOfCards(["♣6","♠3","♠J","♦2","♥3"],["♠8","♥2","♦8","♥9","♦J"]))
console.log(winnerPairOfCards(["♥3","♠9","♦3","♣Q","♦A"],["♥4","♥3","♠10","♦3","♥4"]))
console.log(winnerPairOfCards(["♥3","♠9","♦3","♣Q","♦3"],["♥4","♥A","♠10","♦A","♥4"]))
console.log(winnerPairOfCards(["♣K","♥8","♥K","♠K","♣A"],["♥K","♥4","♣K","♠4","♦K"]))
console.log(winnerPairOfCards(["♥9","♠8","♦7","♣6","♦5"],["♥9","♥8","♠7","♦6","♥4"]))
console.log(winnerPairOfCards(["♥3","♠4","♦5","♣6","♦7"],["♥2","♥3","♠5","♦6","♥7"]))
console.log(winnerPairOfCards(["♥K","♠4","♦K","♣6","♦6"],["♥6","♥K","♠K","♦6","♥7"]))
console.log(winnerPairOfCards(["♥2","♠2","♦2","♣2","♦6"],["♥2","♥2","♠2","♦2","♥7"]))
console.log(winnerPairOfCards(["♥2","♠2","♦2","♣2","♦6","♠3","♦3","♣4","♦6"],["♥2","♥2","♠2","♦3","♥7","♠2","♦3","♣6","♦6"]))
console.log(winnerPairOfCards(["♥2","♠2","♦2","♣2","♦6","♠3","♦3","♣4","♦3"],["♥2","♥2","♠2","♦3","♥7","♠2","♦3","♣6","♦6"]))
console.log(winnerPairOfCards(["♥2","♠2","♦6"],["♥2","♥2","♥3"]))
console.log(winnerPairOfCards(["♥2","♠A","♦6"],["♥2","♥2","♥3"]))
