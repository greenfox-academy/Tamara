'use strict';

var test = require('tape');
var apples = require('./apples.js');

test('write an apple', function (t) {
  var actual = apples('apple');
  var expected = 'pear';

  t.equal(actual, expected);
  t.end();
});
