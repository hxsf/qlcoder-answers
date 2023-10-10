const left = []
const right = []
left[0] = "bcdefghijklmnopqrstuvwzyxABCDEF0".split('')
left[1] = "cdefghijklmnopqrstuvwzyxABCDEF00".split('')
left[2] = "defghijklmnopqrstuvwzyxABCDEF000".split('')
left[3] = "hijklmnopqrstuvwzyxABCDEF0000000".split('')
left[4] = "ijklmnopqrstuvwzyxABCDEF00000000".split('')

left[5] = "11111011101010000000001011000111".split('')



right[0] = "0abcdefghijklmnopqrstuvwzyxABCD0".split('')
right[1] = "01000000000000000000000000000000".split('')

right[2] = "abcdefghijklmnopqrstuvwzyxABCDEF".split('')
right[3] = "00111111111111111111111111111111".split('')

for (var i = 31; i >= 0; --i) {
    let str = '(' + [left[0][i], left[1][i], left[2][i], left[3][i], left[4][i]].join(' + ') + ') ^ ' + left[5][i] +
    ' == ' +
    '(' + right[0][i] + ' & ' + right[1][i] + ') ^ (' + right[2][i] + ' & ' + right[3][i] + ')'
    console.log(str)
}
