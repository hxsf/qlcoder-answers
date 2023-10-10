let ThriftClient = require('thrift-client');

const host = '121.201.63.168'; // Server Host
const port = 9090; // Service Port
const schema = `enum Type {
  GET_ANSWER = 1,
  GET_CREATEDTIME = 2,
  GET_AUTHOR = 3,
}

struct Auth {
  1: string username,
  2: Type type,
}

service Task {
   string getTaskInfo(1:Auth auth),
}
`; // Service Thrift File Contents

let client = new ThriftClient({ host, port, schema });

client.call('getTaskInfo').then(result => {
    console.log(result); // true or false
});
