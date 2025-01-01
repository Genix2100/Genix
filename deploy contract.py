import json
from web3 import Web3

def deploy_contract():
    web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    web3.eth.defaultAccount = web3.eth.accounts[0]

    with open('GNX_contract.sol', 'r') as file:
        contract_source_code = file.read()

    compiled_sol = compile_source(contract_source_code)
    contract_interface = compiled_sol['<stdin>:GNXToken']

    GNXToken = web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

    tx_hash = GNXToken.constructor().transact()
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    print(f'Contract Deployed at Address: {tx_receipt.contractAddress}')

if __name__ == "__main__":
    deploy_contract()
