const fs = require('fs')
const path = require('path')

const img_path = path.resolve(__dirname, './imgs')

if (!fs.existsSync(img_path))
    fs.mkdirSync(img_path)
var index = 1000
const buf = fs.readFileSync(path.resolve(__dirname, './rf.data'))
var p = 0
// console.log(buf.slice(12302, 12302 + 0xc515))
while (buf[p] != null || buf[p] != undefined) {
    console.log('p', p);
    let cur = buf[p]
    let size = 0
    if (cur == 0 || cur == 1) {
        size = buf.readInt32BE(p + 1)
        fs.writeFileSync(path.join(img_path, `${index++}_${cur}`), buf.slice(p + 5, p + 5 + size))
    } else if (cur != 2){
        console.log('error', cur);
        break
    }
    p += size + 5
}
console.log('endl')
