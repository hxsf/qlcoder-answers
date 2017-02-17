const request = require('request')

var url = 'http://www.qlcoder.com/train/spider3/'
var flag = {}
var res = {}
for (var i = 1; i < 11; i++) {
	(function (i) {
		var cnt = 0;
		var clock = setInterval(() => {
			request(url + i, function(err, resp, body) {
				if (res[i] != body) {
					if (flag[i]) {
						console.log(i, cnt)
						clearInterval(clock)
					}
					res[i] = body
					flag[i] = true
					cnt = 0
				}
				cnt++
			})
		}, 1000)
		request(url + i, function(err, resp, body) {
			res[i] = body
		})
	})(i)
}