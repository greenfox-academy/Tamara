'use strict';
let port = 8080;
let response = [
  { "id": 1, "title": "Favorites", "system": 1},
  { "id": 2, "title": "Music for programming", "system": 0},
  { "id": 3, "title": "Driving", "system": 0},
  { "id": 5, "title": "Fox house", "system": 0},
]

const express = require('express');
const app = express();

app.use('/', express.static('./'));
express.json.type = "application/json";
app.use(express.json());

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/main.html');
});

app.get('/playlists', (req, res) => {
  res.json(response);
});



console.log(app.listen(port) + 'server established');