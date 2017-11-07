'use strict';

var test = require('tape');
var sum = require('./sum.js');

test('sum numbers', function (t) {
  var actual = sum([2, 3]);
  var expected = 5;

  t.equal(actual, expected);
  t.end();
});

test('empty list', function (t) {
  var actual = sum([]);
  var expected = 0;

  t.equal(actual, expected);
  t.end();
});

test('return with one element', function (t) {
  var actual = sum([3]);
  var expected = 3;

  t.equal(actual, expected);
  t.end();
});

