function isMountain(height){
    if (height.length < 3) return false

    // 頂点が両サイドにないか判定
    let maxIndex = height.indexOf(height.reduce((a,b) => Math.max(a,b)))
    if (maxIndex == 0 || maxIndex == height.length -1) return false

    // 山頂から下っているか判定
    for (let i = maxIndex; i < height.length; i++) if (height[i] <= height[i + 1]) return false
    for (let i = maxIndex; i >= 0; i--) if (height[i] <= height[i - 1]) return false

    return true
}

console.log(isMountain([1,2,3,2]))
console.log(isMountain([1,2,3,2,1]))
console.log(isMountain([1,2]))
console.log(isMountain([2,1]))
console.log(isMountain([1,2,2,2,2]))
console.log(isMountain([1,2,3]))
console.log(isMountain([4,3,2,1]))
console.log(isMountain([1,2,2,2,3,2]))
console.log(isMountain([3,2,2,2,1,1]))
console.log(isMountain([10,20,30,400,500,10]))
console.log(isMountain([100,200,100,400,500,100]))
console.log(isMountain([100,200,300,200,100,300]))
console.log(isMountain([100,50,100,200,300,400]))
