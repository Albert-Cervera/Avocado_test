#--------------------------------------------------------------------------
# NASA/GSFC, Software Integration & Visualization Office, Code 610.3
#--------------------------------------------------------------------------
#
# MODULE: Mini blockchain project || Avocado Test
# FILE: transferValue.py
# USE: python3 blockchain.py || This script is called by "blockchain.py"
#
#> @author
#> Albert Aaron Cervera Uribe
#
#  DESCRIPTION:
#> This script will aid in the send process of Ether and Tokens between
# accounts.
#
# REVISION HISTORY:
#
# 05 November 2019 - Initial Version
# -- November 2019 - Final Version
#
# MODIFICATIONS:
#
# Initial mod. version: --------
# Final mod. version:   --------
#
# TODO_dd_mmm_yyyy - TODO_describe_appropriate_changes - TODO_name
#--------------------------------------------------------------------------
from web3 import Web3;
from ethtoken.abi import EIP20_ABI;
import manage_account;
import os;

ganache_url = "http://127.0.0.1:7545";
web3 = Web3(Web3.HTTPProvider(ganache_url));

#account1: 0xbaCbA1413958Df714Ed9FAa0ac87Dc3ce0F6e85b
#privateKey: 9a45c3f838d25c13341408f4a5e42126c7743fbc7d05e05e6a17c3f8af53e033

#account2: 0x00A10F1056387155cadc434f4F991a352AbA25ac

def transferMain(account):
    print("\nTransfer Ether/Tokens ----------------------------------------\n");
    print("\nYou now can send Ether to other accounts");
    print("(As well as tokens)\n");
    print("Send Ether: 1  ||  Send Tokens: 2  ||  Return: 3");
    option = input("\nChoose an option: ");
    if (int(option)==1):
        transferEther(account);
    elif (int(option)==2):
        transferTokens(account);
    elif (int(option)==3):
        os.system('clear');
        manage_account.login(account);
    else:
        print("Invalid option");



def transferEther(account):
    os.system('clear');
    print("\nTransfer Ether -----------------------------------------------\n");
    print("Please, write the account that will receive the ETH");
    account2 = input("Account to transfer: ");
    os.system('clear');
    print("\nTransfer Ether -----------------------------------------------\n");
    print("Now write your private key");
    print("\nWARNING: Never let anyone to have your private key");
    print("This program will use it only once to do the transfer and then delete it");
    privateKey = input("\nPrivate Key of your account: ");
    os.system('clear');
    print("\nTransfer Ether -----------------------------------------------\n");
    print("Private Key received\n");
    value = input("Ether amount to send: ");
    gas = input("Gas amount to use: ");
    gasPrice = input("Gas price: ");
    print("Proceed: 1   ||  Cancel: 2");
    option = input("Confirm command: ");
    if (int(option)==1):
        transactionEther(account,account2,privateKey,value,gas,gasPrice);
    elif (int(option)==2):
        os.system('clear');
        manage_account.login(account);
    else:
        print("Invalid option");

def transferTokens(account):
    os.system('clear');
    print("\nTransfer Tokens ----------------------------------------------\n");
    print("Please, write the address that will receive the Tokens");
    contract_address = input("Address to transfer: ");
    os.system('clear');
    print("\nTransfer Tokens ----------------------------------------------\n");
    print("Now write your private key");
    print("\nWARNING: Never let anyone to have your private key");
    print("This program will use it only once to do the transfer and then delete it");
    privateKey = input("\nPrivate Key of your account: ");
    os.system('clear');
    print("\nTransfer Tokens ----------------------------------------------\n");
    print("Private Key received\n");
    token_val = input("Amount of Tokens to send: ");
    gas = input("Gas amount to use: ");
    gasPrice = input("Gas price: ");
    print("Proceed: 1   ||  Cancel: 2");
    option = input("Confirm command: ");
    if (int(option)==1):
        transactionTokens(account, contract_address, privateKey, token_val, gas, gasPrice);
    elif (int(option)==2):
        os.system('clear');
        manage_account.login(account);
    else:
        print("Invalid option");



def transactionEther(account, account2, privateKey, value, gas, gasPrice):
    nonce = web3.eth.getTransactionCount(account);
    tx = {'nonce': nonce,'to': account2,'value': web3.toWei(value, 'ether'), 'gas': int(gas),
    'gasPrice': web3.toWei(int(gasPrice), 'gwei')};

    #Signing transaction
    signed_transaction = web3.eth.account.signTransaction(tx, privateKey);

    #Send transaction to the network
    raw_transaction = web3.eth.sendRawTransaction(signed_transaction.rawTransaction);
    tx_hash = web3.toHex(raw_transaction);
    print("\nTransaction hash in hexbyte: " + str(tx_hash));

    txtEther(account, account2, value, gas, gasPrice, tx_hash);
    print("Operation completed");
    print("\nThe file '02_Transaction_Completed.txt' has been succesfully updated");
    input("\nPress enter to return");
    os.system('clear');
    manage_account.login(account);

def transactionTokens(account, contract_address, privateKey, token_val, gas, gasPrice):

    nonce = w3.eth.getTransactionCount(account);
    contract_add = w3.toChecksumAddress(contract_address);
    contract = w3.eth.contract(contract_add, abi = EIP20_ABI);
    tx_contract = contract.functions.transfer(contract_address,token_val).buildTransaction({'chainId':1,
    'gas':gas, 'value': 0, 'gasPrice': web3.toWei(int(gasPrice), 'gwei'),'nonce': nonce});

    #Signing transaction
    signed_transaction = web3.eth.account.signTransaction(tx_contract, privateKey);

    #Send transaction to the network
    raw_transaction = web3.eth.sendRawTransaction(signed_transaction.rawTransaction);
    tx_hash = web3.toHex(raw_transaction);
    print("\nTransaction hash in hexbyte: " + str(tx_hash));

    txtTokens(account, contract_address, token_val, gas, gasPrice, tx_hash);
    print("\nThe file '03_Transaction_Token_Completed.txt' has been succesfully updated");
    input("\nPress enter to return");
    os.system('clear');
    manage_account.login(account);



def txtEther(account, account2, value, gas, gasPrice, tx_hash):
    fl = open("02_Transaction_Completed.txt","w+"); #write file, if doesn't exists, create it!
    fl.write("Newest transaction information ------------------------------\n");
    fl.write("\nAccount that made the transaction: " + str(account));
    fl.write("\nAccount that received the transaction: " + str(account2));
    fl.write("\n\nEther value: " + str(value));
    fl.write("\nGas amount used: " + str(gas));
    fl.write("\nGas price: " + str(gasPrice));
    fl.write("\n\nTransaction hash in hexbyte: " + str(tx_hash));
    fl.write("\n\nEnd of file\n");
    fl.close();

def txtTokens(account, contract_address, token_val, gas, gasPrice, tx_hash):
    fl = open("03_Transaction_Token_Completed.txt","w+"); #write file, if doesn't exists, create it!
    fl.write("Newest transaction information ------------------------------\n");
    fl.write("\nAccount that made the transaction: " + str(account));
    fl.write("\nAcddress that received the transaction: " + str(contract_address));
    fl.write("\n\nToken value sent: " + str(token_val));
    fl.write("\nGas amount used: " + str(gas));
    fl.write("\nGas price: " + str(gasPrice));
    fl.write("\n\nTransaction hash in hexbyte: " + str(tx_hash));
    fl.write("\n\nEnd of file\n");
    fl.close();

# Faculty of Mathematics at Merida, Yucatan
