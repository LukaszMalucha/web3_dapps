const path = require("path");
const fs = require("fs");
const solc = require("solc");

// Root Directory
const inboxPath = path.resolve(__dirname, 'contracts', 'Inbox.sol');
const source = fs.readFileSync(inboxPath, 'utf8');

//// Compile Statement - 1 stands for number of contracts to compile
console.log(solc.compile(source, 1));


