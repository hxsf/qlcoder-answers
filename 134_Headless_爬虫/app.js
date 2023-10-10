console.log('123')
var page = require('webpage').create();
page.open('https://www.baidu.com', function(status) {
    console.log("Status: " + status)
    var title = page.evaluate(function () {
        return document.title
    })
    console.log(title)

    phantom.exit()
})
