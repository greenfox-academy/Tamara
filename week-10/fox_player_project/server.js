'use strict';

const express = require('express');
const app = express();

app.use('/', express.static('./'));
express.json.type = "application/json";
app.use(express.json());

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/main.html');
});

app.get('/hello', (req, res) => {
  res.send('hello world!');
});

app.listen(8080);