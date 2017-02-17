const fs = require('fs')

const str = fs.readFileSync('./uv.txt', 'utf8')
const arr = str.split(/(\r?\n)+/)
var cnt = 0
var users = new Set()
var re = /^2015-08-24_\d\d:\d\d:\d\d (\d+) (\w+)$/
for (let item of arr) {
    var res = item.match(re)
    if (res && res[1] && res[2]) {
        if (!users.has(res[1])) {
            users.add(res[1])
            cnt++
        }
    }
}

console.log(cnt);
