'use strict'

var express = require('express');
var app = express();

app.use('/assets', express.static('./assets'));
express.json.type = 'application/json';
app.use(express.json());

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function(req, res) {
  if (req.query.input) {
    res.json({
      'received': req.query.input*1,
      'result': req.query.input*2
    });
  } else {
      res.json({
        'error': 'Please provide an input!'
    }); 
  };
});


app.get('/greeter', function(req, res) {
  console.log(req.query)
  if (req.query.name && req.query.title) {
    res.json({
     'welcome_message': 'Oh, hi there ' + req.query.name + ', my dear ' + req.query.title + '!'
    });
  } else if (req.query.name && !req.query.title) {
    res.json({
      'error': 'Please provide a title!'
    })
  } else {
    res.json({
      'error': 'Please provide a name!'
    })
  }
});


app.get('/appenda/:appendable', function(req, res) {
  res.json({
    'appended': req.params.appendable + 'a'
  });
});
  

app.post('/dountil/:what', function(req, res) {
  if (!req.params.what) {
    res.json({
      'error': 'Please provide a number!'
    });
  } else if (req.params.what === 'sum') {
    let sum = 0;
    let num = req.body.until;
    while (num > 0){
      sum += num;
      num--;
    }
  res.json({
    'result': sum 
  });
  } else if (req.params.what === 'factor') {
    let fact = 1;
    let num = req.body.until;
    while (num > 0){
      fact *= num;
      num--;
    }  
  res.json({
    'result': fact 
    });
  };
});


app.post('/arrays', function(req, res) {
  if (!req.params.what || num === 0) {
    res.json({
      'error': 'Please provide what to do with the numbers!'
    });
  } else if (req.params.what === 'sum' && num === [1, 2, 5, 10]) {
      let sum = 0;
      let num = req.body.until;
      for (let i = 0; i < num.length; i++) {
        sum += num;
      }
  console.log(res.json({
    'result': sum 
  }));
  } else if (req.params.what === 'multiply' && num === [1, 2, 5, 10]) {
      let multiply = 0;
      let num = req.body.until;
      for (let i = 0; i < num.length; i++) {
        multiply *= num;
      }
  console.log(res.json({
    'result': multiply 
  }));
  } else if (req.params.what === 'double' && num === [1, 2, 5, 10]) {
      let double = [];
      let num = req.body.until;
      for (let i = 0; i < num.length; i++) {
        num *= 2;
        double.push(num);
      }
  console.log(res.json({
    'result': double
  }));
  };
});

app.listen(8080, () => {console.log('Server is running')});
