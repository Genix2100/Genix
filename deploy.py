python
import time
from solcx import compile_source
from web3 import Web3

Exemplu simplu de contract Solidity
contract_source_code = '''
pragma solidity ^0.8.0;

contract HelloWorld {
    string public greeting = "Salut, GENIX!";
}
'''

Compilează contractul
compiled_sol = compile_source(contract_source_code)
contract_id, contract_interface = compiled_sol.popitem()

Conectare la rețeaua locală (ex: Ganache)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

Setează contul implicit (asigură-te că acest cont există în rețeaua ta locală)
w3.eth.default_account = w3.eth.accounts[0]

Creează instanța contractului
HelloWorld = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

Trimite tranzacția pentru a implementa contractul
tx_hash = HelloWorld.constructor().transact()

Așteaptă confirmarea tranzacției
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f'Contractul a fost implementat la adresa: {tx_receipt.contractAddress}')


---
