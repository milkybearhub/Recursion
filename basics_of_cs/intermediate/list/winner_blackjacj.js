function winnerBlackjack(playerCards,houseCards){
    const playerScore = calcScore(playerCards)
    // プレイヤーの手札の合計値が 21 を超えている場合はプレイヤーの敗北
    if (playerScore > 21) return false

    const houseScore  = calcScore(houseCards)
    // ディーラーの手札の合計値が 21 を超えている場合はプレイヤーの勝利
    if (houseScore > 21) return true

    // プレイヤーの手札の合計値がディーラーのそれを上回る場合はプレイヤーの勝利
    if (playerScore > houseScore) return true

    // 両者同じ合計値の場合はプレイヤーの敗北
    return false
}

function calcScore(cards) {
    // Learn: 先頭を1として配列のインデックスを使って変換する方が賢い
    // ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    for (let i = 0; i < cards.length; i ++) {
        const number = cards[i].substring(1, 3)
        switch (number) {
            case "A":
                cards[i] = 1
                break
            case "J":
                cards[i] = 11
                break
            case "Q":
                cards[i] = 12
                break
            case "K":
                cards[i] = 13
                break
            default:
                cards[i] = number
                break
        }
    }

    return cards.map(value => Number(value)).reduce((sum, element) => sum + element, 0)
}

console.log(winnerBlackjack(["♣4","♥7","♥7"],["♠Q","♣J"]))
console.log(winnerBlackjack(["♥10","♥6","♣K"],["♠Q","♦2","♥K"]))
console.log(winnerBlackjack(["♠3","♠J","♣5"],["♣A","♥Q","♣5"]))
console.log(winnerBlackjack(["♥2","♣A","♣8","♥7","♥3"],["♥6","♥K","♣5","♥K"]))
console.log(winnerBlackjack(["♥2","♣A","♣8","♥7","♥3"],["♥2","♣A","♣8","♥7","♥3"]))
