const assert = require('assert');
const ganache = require('ganache-cli');
// Constructor
const Web3 = require('web3');
// Instance
const web3 = new Web3(ganache.provider());
const { interface, bytecode } = require('../compile');

let accounts;
let inbox;


beforeEach(async () => {
//  List accounts and use on e of them to deploy contract
  accounts = await web3.eth.getAccounts();

  inbox = await new web3.eth.Contract(JSON.parse(interface))
    .deploy({ data: bytecode, arguments: ["Hi all!"] })
    .send({ from: accounts[0], gas: '1000000' });
});

describe('Inbox', () => {
  it('deploys a contract', () => {
    assert.ok(inbox.options.address);
  });
  it('has a default message', async () => {
    const message = await inbox.methods.message().call();
    assert.equal(message, "Hi all!");
  });
  it('changes the message', async () => {
    await inbox.methods.setMessage("hello").send({from: accounts[0]});
    const message = await inbox.methods.message().call();
    assert.equal(message, "hello");
  });

});













//class Car {
//  park() {
//    return 'stopped';
//  }
//
//  drive() {
//    return 'vroom';
//  }
//}
//
//// Initialize variable
//let car;
//
//beforeEach(() => {
//  car = new Car();
//});
//
//describe("Car Class", () => {
//  it('park function', () => {
//    assert.equal(car.park(), 'stopped');
//  });
//});
//
//




