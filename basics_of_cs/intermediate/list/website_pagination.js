function websitePagination(urls, pageSize, page){
    let answer = []
    let startPosition = pageSize * (page -1)
    let count = 0
    for (let i = startPosition; count < pageSize; i++) {
        if (i > urls.length - 1) break

        answer.push(urls[i])
        count ++
    }
    return answer
}

console.log(websitePagination(["url1","url2","url3","url4","url5","url6"],4,1))
console.log(websitePagination(["url1","url2","url3","url4","url5","url6","url7","url8","url9"],3,2) )
console.log(websitePagination(["url1","url2","url3","url4","url5","url6","url7","url8","url9"],4,3))