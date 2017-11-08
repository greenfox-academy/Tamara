'use strict';

var test = require('tape');
var counter = require('./count_letters.js');

test('one letter', function (t) {
  var actual = counter("b");
  var expected = {'b': 1};

  t.equal(actual, expected);
  t.end();
});
