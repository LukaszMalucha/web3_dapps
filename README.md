# Web 3.0 Dapps


## Requirements

#### Ganache

https://trufflesuite.com/ganache/

#### Truffle Framework

npm install -g truffle

#### MetaMask

https://metamask.io/


## Commands

#### Init

`truffle init`

#### Compile

`truffle compile`

#### Migrate

`truffle migrate`

### Truffle Console

`todoList = await TodoList.deployed()`

`todoList.address`

`todoList.count`
`taskCount = await todoList.taskCount()`
`taskCount.toNumber()`
`task = await todoList.tasks(1)`
`task.id.toNumber()`



