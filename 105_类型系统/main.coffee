fs = require 'fs'

code = fs.readFileSync './src/145743685778441.txt', 'utf8'
arr = code.split /\s*\r?\n/

re_type = /^type +(\w+)$/
re_new = /^(\w+) *:= *new +(\w+)$/
re_var = /^(\w+) *:= *(\w+)$/

types = new Map()
vars = new Map()

result = new Array()
for item in arr
    if res = re_type.exec item
        name = res[1]
        types[name] = name
    else if res = re_new.exec item
        name = res[1]
        type = res[2]
        if types.has type
            unless vars[name]
                vars[name] ?= type
                result.push "#{name} - #{type}"
    else if res = re_var.exec item
        name = res[1]
        value = res[2]
        if vars[value]
            unless vars[name]
                vars[name] = vars[value]
                result.push "#{name} - #{type}"
    else if /^\w+ = (new )?\w+$/.test item

    else
        console.error item


console.log result.sort().join ' - '
