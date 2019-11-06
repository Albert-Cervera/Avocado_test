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
# -- November 2019 - Final Version
#
# MODIFICATIONS:
#
# Initial mod. version: --------
# Final mod. version:   --------
#
# TODO_dd_mmm_yyyy - TODO_describe_appropriate_changes - TODO_name
#--------------------------------------------------------------------------
from eth_account import Account;
import blockchain;

"""
Function: createAccount
Input: --
Returns: --
Description: It creates a new account locally
"""
def createAccount():
    print("\n ---------------- New account ----------------");
    entropy_label = input("Please, add an entropy label to create account: ");
    new_acct = Account.create(entropy_label);
    new_acct_address = new_acct.address;
    new_private_key = new_acct.privateKey;
    print('\nThe new account address is: {}'.format(new_acct_address));
    print('The new private key is: {}'.format(new_private_key.hex()));
    print("The key is: {}".format(new_acct.key));
    txtGenerator(entropy_label, new_acct_address, new_private_key);
    print("\nThe file '01_Account_Info.txt' has been succesfully updated");
    enter = input("\nPress enter to return to the main options");
    os.system('clear')
    blockchain.main();



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
sign this transaction and broadcast it into the network.
"""
def transactionAccount(new_acct_address, new_private_key):

    nonce = web3.eth.getTransactionCount(new_acct_address);
    tx = {'nonce': nonce,'value': 0, 'gas': 2000000,
    'gasPrice': web3.eth.gasPrice};

    #Signing transaction
    signed_transaction = web3.eth.account.signTransaction(tx, new_private_key);

    #Send transaction to the network
    raw_transaction = web3.eth.sendRawTransaction(signed_transaction.rawTransaction);
    tx_hash = web3.toHex(raw_transaction);
    print("\nTransaction hash of new account in hexbyte: " + str(tx_hash));

    #Write transaction on file
    fl = open("01_Account_Info.txt","w+"); #write file, if doesn't exists, create it!
    fl.write("\n\nNew account transaction information -------------------------\n");
    fl.write("Transaction hash in hexbyte: " + str(tx_hash));
    fl.write("\n\nEnd of file\n");
    fl.close();
    print("\nThe file '01_Account_Info.txt' has been succesfully updated");
    enter = input("\nPress enter to return to the main options");
    os.system('clear')
    blockchain.main();




# Faculty of Mathematics at Merida, Yucatan
