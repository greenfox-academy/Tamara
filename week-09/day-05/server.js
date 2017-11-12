'use strict';

const express = require('express');
const app = express();

app.use('/assets', express.static('./assets'));
express.json.type = "application/json";
app.use(express.json());

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/reddit2_project.html');
});

app.get('/hello', (req, res) => {
  res.send('hello world!');
});

app.listen(8080);