#--------------------------------------------------------------------------
# NASA/GSFC, Software Integration & Visualization Office, Code 610.3
#--------------------------------------------------------------------------
#
# MODULE: Mini blockchain project || Avocado Test
# FILE: blockchain.py
# USE: python3 blockchain.py
#
#> @author
#> Albert Aaron Cervera Uribe
#
#  DESCRIPTION:
#> The quick brown fox jumps over the lazy dog
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
import create_account;
import manage_account;
import os;
from web3 import Web3;

infura_url = "https://ropsten.infura.io/v3/963aa3c429b5444cb0e007241f8bf0fd";
web3 = Web3(Web3.HTTPProvider(infura_url));
print("Assert web3 connection: " + str(web3.isConnected()));
print("Block number of web3: " + str(web3.eth.blockNumber))

"""
Function: main
Input: --
Returns: --
Description: Allows the flow control of the program
"""
def main():
    print("\nWelcome to Ethereum blockchain test tool\n");
    print("1: Log account");print("2: Create account");
    option = input("Choose an option: ");
    optionSelection(option);

"""
Function: optionSelection
Input: option
Returns: --
Description: Aids in the management of the options from main()
"""
def optionSelection(option):
    if (int(option) == 1):
        print("\n ---------------- Account login ----------------");
        account = input("Public key: ");
        os.system('clear')
        manage_account.login(account);
    elif(int(option) == 2):
        print("\n ---------------- New account ----------------");
        print("1: Create account");print("2: Sign and validate account");
        option = input("Choose an option: ");
        if (int(option) == 1):
            create_account.createAccount();
        elif (int(option) == 2):
            print("\n ---------------- Sign and validate account ----------------");
            print("Add your address and private key");
            print("You could find them in the '01_Account_Info.txt' file");
            print("\nWARNING: Never let anyone to have your private key\n");
            print("You may need some Ether to do the transaction");
            address = input("\nAddress of new created account");
            private_key = input("Private key of new account");
            transactionAccount(address, private_key);
        else:
            print("Invalid option");



#Calling main function
main();



# Faculty of Mathematics at Merida, Yucatan
