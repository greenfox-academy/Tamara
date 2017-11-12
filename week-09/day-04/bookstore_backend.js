'use strict';

const express = require('express');
const app = express();
const mysql = require('mysql');

app.use('/assets', express.static('./assets'));
express.json.type = "application/json";
app.use(express.json());

const con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'mysql',
  database: 'bookstore'
});

con.connect((err) => {
  if(err){
    console.log('Error connecting to MYSQL\n');
    return;
  }
  console.log('MYSQL connection established');
});

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/bookstore.html');
});

app.get('/books', (request, response) => {
  con.query('SELECT book_name FROM book_mast;', function(error, rows) {
    if (error) {
      console.log(error.toString());
    }
   response.json(rows);
  });
});

app.listen(8080);