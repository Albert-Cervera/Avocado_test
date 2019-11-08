#--------------------------------------------------------------------------
# NASA/GSFC, Software Integration & Visualization Office, Code 610.3
#--------------------------------------------------------------------------
#
# MODULE: Mini blockchain project || Account creator
# FILE: create_account.py
# USE: python3 blockchain.py || This script is called by "blockchain.py"
#
#> @author
#> Albert Aaron Cervera Uribe
#
#  DESCRIPTION:
#> This script will allow creation of a blockchain account.
#
# REVISION HISTORY:
#
# 04 November 2019 - Initial Version
# 07 November 2019 - Final Version
#
# MODIFICATIONS:
#
# Initial mod. version: --------
# Final mod. version:   --------
#
# TODO_dd_mmm_yyyy - TODO_describe_appropriate_changes - TODO_name
#--------------------------------------------------------------------------
from eth_account import Account;
from ethtoken.abi import EIP20_ABI;

"""
Function: createAccount
Input: --
Returns: --
Description: It creates a new account locally generating a public and
private key.
"""
def createAccount():
    print("\n ---------------- New account ----------------");
    entropy_label = input("Please, add an entropy label to create account: ");
    new_acct = Account.create(entropy_label);
    new_acct_address = new_acct.address;
    new_private_key = new_acct.privateKey;
    print('\nThe new account address is: {}'.format(new_acct_address));
    print('The new private key is: {}'.format(new_private_key.hex()));
    txtGenerator(entropy_label, new_acct_address, new_private_key);
    print("\nThe file '01_Account_Info.txt' has been succesfully updated");



"""
Function: txtGenerator
Input: entropy_label, new_acct_address, new_private_key
Returns: txt file
Description: Generates a txt file with sensitive information of the created acc.
"""
def txtGenerator(entropy_label, new_acct_address, new_private_key):
    fl = open("01_Account_Info.txt","w+"); #write file, if doesn't exists, create it!
    fl.write("Newest account information-----------------------------------\n");
    fl.write("\nEntropy label: " + str(entropy_label));
    fl.write("\nAddress (public key): " + str(format(new_acct_address)));
    fl.write("\nPrivate key: " + str(format(new_private_key.hex())));
    fl.write("\n\n---------------------------------------------------------\n");
    fl.close();


"""
Function: transactionAccount
Input: new_acct_address, new_private_key
Returns: overwrites the txt file
Description: It creates a new transaction for the new created account, then it
signs this transaction and broadcast it into the network.
"""
def transactionAccount(new_acct_address, new_private_key, web3):

    nonce = web3.eth.getTransactionCount(new_acct_address);

    #Bytecode of our 'contract.sol' file
    contract_bytecode = "60806040526040805190810160405280600c81526020017f48656c6c6f2c576f726c642100000000000000000000000000000000000000008152506000908051906020019061004f929190610062565b5034801561005c57600080fd5b50610107565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100a357805160ff19168380011785556100d1565b828001600101855582156100d1579182015b828111156100d05782518255916020019190600101906100b5565b5b5090506100de91906100e2565b5090565b61010491905b808211156101005760008160009055506001016100e8565b5090565b90565b6101a4806101166000396000f300608060405260043610610041576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806303e33b5314610046575b600080fd5b34801561005257600080fd5b5061005b6100d6565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561009b578082015181840152602081019050610080565b50505050905090810190601f1680156100c85780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b606060008054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561016e5780601f106101435761010080835404028352916020019161016e565b820191906000526020600020905b81548152906001019060200180831161015157829003601f168201915b50505050509050905600a165627a7a723058200bd694f7a339a46999d68b508db4ccef37a5dd4361bae02ae694c446d53fbfce0029";

    contract = web3.eth.contract(abi = EIP20_ABI, bytecode = contract_bytecode);
    tx = contract.constructor().buildTransaction({'nonce': nonce});

    #Signing transaction
    signed_transaction = web3.eth.account.signTransaction(tx, new_private_key);

    #Send transaction to the network
    raw_transaction = web3.eth.sendRawTransaction(signed_transaction.rawTransaction);
    tx_hash = web3.toHex(raw_transaction);

    tx_receipt = w3.eth.waitForTransactionReceipt(raw_transaction, timeout = 120, poll_latency = 0.1);
    print("\nTransaction hash of new account in hexbyte: " + str(tx_hash));

    #Write transaction on file
    fl = open("01_Account_Info.txt","w+"); #write file, if doesn't exists, create it!
    fl.write("\n\nNew account transaction information -------------------------\n");
    fl.write("Transaction hash in hexbyte: " + str(tx_hash));
    fl.write("\n\nEnd of file\n");
    fl.close();
    print("\nThe file '01_Account_Info.txt' has been succesfully updated");


# Faculty of Mathematics at Merida, Yucatan
