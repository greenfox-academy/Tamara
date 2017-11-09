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
});

con.connect((err) => {
  if(err){
    console.log('Error connecting to MYSQL');
    return;
  }
  console.log('MYSQL connection established');
});



app.listen(3000);
