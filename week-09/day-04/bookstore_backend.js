'use strict';

const express = require('express');
const app = express();
const mysql = require('mysql');
let bookDetails = 'SELECT book_name, aut_name, cate_descrip, pub_name, book_price' + 
                  ' FROM book_mast' +
                  ' JOIN author ON book_mast.aut_id = author.aut_id JOIN category ON book_mast.cate_id = category.cate_id JOIN publisher ON book_mast.pub_id = publisher.pub_id ';

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
/*
app.get('/books', (request, response) => {
  con.query('SELECT book_name FROM book_mast', function(error, rows) {
    if (error) {
      console.log(error.toString());
    }
   response.json(rows);
  });
});
*/

let renderBookDetails = function(item) {
  item.forEach(function(item) {
      let tempBook = document.createElement('td');
      tempBook.innerText = item.book_name +
                           item.aut_name +
                           item.cate_descrip +
                           item.pub_name +
                           item.book_price;
      document.body.appendChild(tempBook);
  });
};

// function getDatabase(tableName, what, callback) {
//   let searchQuery = 'SELECT' + what + 'FROM ' + tableName;
//   con.query(searchQuery, function(error, results, fields){
//     callback(results, what);
//   });
// };

app.get('/books', function(req, res){
  let filters = {
    category: req.query.category,
    publisher: req.query.publisher,
    plt: req.query.plt,
    pgt: req.query.pgt
  }   
  let searchQuery = 'SELECT book_name, aut_name, cate_descrip, pub_name, book_price' + 
    ' FROM book_mast' +
    ' JOIN author ON book_mast.aut_id = author.aut_id JOIN category ON book_mast.cate_id = category.cate_id JOIN publisher ON book_mast.pub_id = publisher.pub_id ';
  let whereAdded = false;

  if (filters.category !== undefined) {
    if (whereAdded) {
      searchQuery+= " AND ";
    } else {
      searchQuery+= " WHERE ";
      whereAdded = true;
    }
    searchQuery+= " cate_descrip='" + filters.category + "'";    
  }

  if (filters.publisher !== undefined) {
    if(whereAdded){
      searchQuery+= " AND ";
    }else{
      searchQuery+= " WHERE ";
      whereAdded = true;
    }
    searchQuery+= " pub_name='" + filters.publisher + "'";  
  }

  con.query(searchQuery, function(error, rows) {
    if (error) {
      console.log(error.toString());
    }
   res.json(rows);
  });
})

app.listen(8080, () => {console.log('Server is running')});
