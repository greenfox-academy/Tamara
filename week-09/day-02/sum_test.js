'use strict';

var test = require('tape');
var sum = require('./sum.js');

test('sum numbers', function (t) {
  var actual = sum([2, 3]);
  var expected = 5;

  t.equal(actual, expected);
  t.end();
});
