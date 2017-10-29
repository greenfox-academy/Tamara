'use strict';

var accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

// Create function that returns the name and balance of cash on an account

// Create function that transfers an amount of cash from one account to another
// it should have three parameters:
//  - from account_number
//  - to account_number
//  - amount of cash to transfer
//
// Log "404 - account not found" if any of the account numbers don't exist to the console.

function nameWithBalance () {
  accounts.forEach(function(e) {
    console.log(e.client_name + ': ' + e.balance);
  })
}

nameWithBalance()

function transferCash (from_account_number, to_account_number, amount) {
  let fromAccount;
  let toAccount;
  for (let i = 0; i < accounts.length; i++) {
    if (from_account_number === accounts[i].account_number) {
      fromAccount = accounts[i];
    } 
    if (to_account_number === accounts[i].account_number) {
      toAccount = accounts[i];
    }
  }
  
  if (fromAccount === undefined || toAccount === undefined) {
      console.log("404 - account not found")
  } 
  toAccount.balance += amount;
  fromAccount.balance -= amount;
  console.log(accounts);
}

transferCash(43546731,11234543, 20)