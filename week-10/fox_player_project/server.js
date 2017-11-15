'use strict';

let port = 8080;
let templatePlayList = [
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
  res.json(templatePlayList);
});

app.post('/playlists', (req, res) => {
  let id = templatePlayList[templatePlayList.length - 1].id + 1;
  templatePlayList.push({"id":id, "title": req.body.titleName, "system": 0});
  console.log(templatePlayList)
  res.json(templatePlayList);
});



app.listen(port, function () {console.log('server established')});