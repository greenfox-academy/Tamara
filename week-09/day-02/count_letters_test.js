'use strict';

var test = require('tape');
var counter = require('./count_letters.js');

test('one letter', function (t) {
  var actual = counter('b');
  var expected = {'b': 1};

  t.deepEqual(actual, expected);
  t.end();
});

test('three letters', function (t) {
  var actual = counter('yaa');
  var expected = {'y': 1, 'a': 2};

  t.deepEqual(actual, expected);
  t.end();
});

test('empty string', function (t) {
  var actual = counter('');
  var expected = {};

  t.deepEqual(actual, expected);
  t.end();
});
