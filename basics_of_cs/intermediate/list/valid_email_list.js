function validEmailList(emailList) {
    let result = []
    for (let i = 0; i < emailList.length; i++) {
        // スペースが存在したら除く
        if (emailList[i].indexOf(" ") != -1) continue

        const domain = emailList[i].substring(emailList[i].indexOf("@") + 1)
        // ドメイン部分に「@」が存在したら除く & 「.」がなければ除く
        if (domain.indexOf("@") != -1 || domain.indexOf(".") == -1) continue

        result.push(emailList[i])
    }

    return result
}

console.log(validEmailList(["ccc@aaa.com","c@cc@aaa.com","cc c@aaa.com","cc.c@aaa.com"]))
console.log(validEmailList(["c@cc@aaa.com","cc c@aaa.com","cc.c@aaacom"]))
console.log(validEmailList(["ccc@aaa.com","cvsd@a.com","tele@bb.aa","cc.c@aaa.com"]))
console.log(validEmailList(["c@cc@aaa.com","tele@bb.aa","cc.c@aaa.com","ccc@aaa.com"]))
