'use strict';

let port = 8080;
// let templatePlayList = [
//   { "id": 1, "title": "Favorites", "system": 1},
//   { "id": 2, "title": "Music for programming", "system": 0},
//   { "id": 3, "title": "Driving", "system": 0},
//   { "id": 5, "title": "Fox house", "system": 0},
// ]

const express = require('express');
const app = express();
const mysql = require('mysql');

var connection = mysql.createConnection({
  host : 'localhost',
  user: 'root',
  password: 'mysql',
  database: 'musiclist'
});
connection.connect((err) => {
  if(err){
    console.log('Error connecting to MYSQL\n');
    return;
  };
  console.log('MYSQL connection established');
});

app.use('/', express.static('./'));
express.json.type = "application/json";
app.use(express.json());

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/main.html');
});

app.get('/playlists', (req, res) => {
  let data = []
  connection.query('SELECT * FROM Playlist;', function(err, result, fields) {
    result.forEach(function(element) {
      data.push(element.name);
    });
    res.json(data);
  });
});

app.post('/playlists', (req, res) => {
   let data = [];
   connection.query("INSERT INTO Playlist (name, system) VALUES ('"+ req.body.name +"', 0)", function(err, result, fields) {
      data.push(req.body.name);
    });
    res.json(req.body.name);
  });

app.get('/playlists/tracklist', (req, res) => {
  let data = []
  connection.query('SELECT * FROM Music;', function(err, result, fields) {
    result.forEach(function(element) {
      data.push(element.title);
    });
    res.send(data);
  });
});



app.listen(port, function () {console.log('server established')});