const pinyin = require('pinyin')
const fs = require('fs')

var txt = fs.readFileSync('./145630854135681.txt', 'utf8')

for (var line of txt.split(/\s+/)) {
    if (line) {
        console.log(pinyin("中心", {
            style: pinyin.STYLE_NORMAL,
            heteronym: true,
            segment: true,
        }));
    }
}
