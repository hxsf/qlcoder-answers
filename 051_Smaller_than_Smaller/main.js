var str1 = '^BABABABANANABABABABABANANABABABABABANANABANANANAAHH|'

function bwt (str) {
    var arr = str.split('')
    var res = [str]
    for (var i = 1; i < arr.length; i++) {
        arr.unshift(arr.pop())
        res.push(arr.join(''))
    }
    res = res.sort()
    var ret = ""
    for (var item of res) {
        ret += item[item.length - 1]
    }
    return ret
}

function RLC (str) {
    console.log(str)
    var re = /([\w\^\|])(\1*)/g
    var res
    var ret = ""
    while (res = re.exec(str)) {
        if (res[0].length > 9) {
            ret += (res[1] + 9).repeat(parseInt(res[0].length / 9)) + res[1] + (res[0].length % 9)
        } else {
            ret += res[1] + res[0].length
        }
    }
    return ret
}

console.log(RLC(bwt(str1)))
