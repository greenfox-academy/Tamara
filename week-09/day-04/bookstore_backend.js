'use strict';

const express = require('express');
const app = express();
const mysql = require('mysql');
app.use('/assets', express.static('./assets'));
express.json.type = 'application/json';
app.use(express.json());

const con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'mysql',
  database: 'bookstore'
});

con.connect((err) => {
  if (err) {
    console.log('Error connecting to MYSQL\n');
    return;
  }
  console.log('MYSQL connection established');
});

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/bookstore.html');
});

app.get('/books', function(req, res) {
  let filters = {
    category: req.query.category,
    authors: req.query.authors,
    publisher: req.query.publisher,
    plt: req.query.plt,
    pgt: req.query.pgt
  }
  var searchQuery = 'SELECT book_name, aut_name, cate_descrip, pub_name, book_price' + 
  ' FROM book_mast' +
  ' JOIN author ON book_mast.aut_id = author.aut_id JOIN category ON book_mast.cate_id = category.cate_id JOIN publisher ON book_mast.pub_id = publisher.pub_id ';
  let whereAdded = false;

  if (filters.category !== undefined) {
    if (whereAdded) {
      searchQuery += ' AND ';
    } else {
      searchQuery += ' WHERE ';
      whereAdded = true;
    }
    searchQuery += " cate_descrip='" + filters.category + "'";    
  }

  if (filters.authors !== undefined) {
    if (whereAdded) {
      searchQuery += ' AND ';
    } else {
      searchQuery += ' WHERE ';
      whereAdded = true;
    }
    searchQuery += " aut_name='" + filters.authors + "'";  
  }
  
  if (filters.publisher !== undefined) {
    if (whereAdded) {
      searchQuery += ' AND ';
    } else {
      searchQuery += ' WHERE ';
      whereAdded = true;
    }
    searchQuery += " pub_name='" + filters.publisher + "'";  
  }

  if (filters.plt !== undefined) {
    if (whereAdded) {
      searchQuery += ' AND ';
    } else {
      searchQuery += ' WHERE ';
      whereAdded = true;
    }
    searchQuery += " book_price<'" + filters.plt + "'";  
  }

  if (filters.pgt !== undefined) {
    if (whereAdded) {
      searchQuery += ' AND ';
    } else {
      searchQuery += ' WHERE ';
      whereAdded = true;
    }
    searchQuery += " book_price>'" + filters.pgt + "'";  
  }

  con.query(searchQuery, function(error, rows) {
    if (error) {
      console.log(error.toString());
    }
    res.send(rows);
  });
})

app.listen(8080, () => {console.log('Server is running')});
