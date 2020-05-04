var http = require('follow-redirects').http;
var fs = require('fs');

var options = {
  'method': 'POST',
  'hostname': '127.0.0.1',
  'port': 5000,
  'path': '/discuss',
  'headers': {
    'Content-Type': 'application/json'
  },
  'maxRedirects': 20
};

var req = http.request(options, function (res) {
  var chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function (chunk) {
    var body = Buffer.concat(chunks);
    console.log(body.toString());
  });

  res.on("error", function (error) {
    console.error(error);
  });
});

var postData = JSON.stringify({"username":"廚房污濁的魚","password":"HKBNBlowWater167!","replyContent":"可以打俾HKBN SALES問下","postID":29035159});

req.write(postData);

req.end();