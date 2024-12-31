const Web3 = require('web3');
const web3 = new Web3('http://localhost:8545'); // Adresa nodului tău GENIX

// Crează un cont
const account = web3.eth.accounts.create();
console.log("Your new wallet address is:", account.address);

// Trimite un mesaj criptat
const message = "GENIX will never fall!";
const signedMessage = web3.eth.accounts.sign(message, account.privateKey);
console.log("Signed message:", signedMessage);
