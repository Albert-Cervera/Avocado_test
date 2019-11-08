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
#> This is the "main script" of the Avocado mini project.
# Main functions include but are not limited to:
# 1) Wallet account creation
# 2) Login of accounts with its public address
# 3) Balance and transactions information from accounts
# 4) Last 12 transactions retrieval and transaction filtering
# 5) Transfer of Ether between accounts
# 6) Transfer of Tokens between accounts
# 7) Exploration of blocks from blockchain
# 8) Filtering of blocks by number
#
# DISCLAIMER:
# I've developed this project as a candidate for Avocado Blockchain Services,
# for this reason, the following code should not be intended for
# "actual professional" use.
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
import os;
import manage_account;
import create_account;
from web3 import Web3;
import explore_blocks;

os.system('clear');
infura_url = "https://ropsten.infura.io/v3/963aa3c429b5444cb0e007241f8bf0fd";
web3 = Web3(Web3.HTTPProvider(infura_url));


"""
Function: main
Input: --
Returns: --
Description: Allows the flow control of the program
"""
def main():
    print("Assert web3 connection: " + str(web3.isConnected()));
    print("Block number of web3: " + str(web3.eth.blockNumber));
    print("\nWelcome to Ethereum blockchain test tool\n");
    print("1: Log account");print("2: Create/Validate account");
    print("3: Explore blockchain blocks");
    option = input("\nChoose an option: ");
    optionSelection(option);

"""
Function: optionSelection
Input: option (input from main)
Returns: --
Description: Aids in the management of the options from main()
"""
def optionSelection(option):
    if (int(option) == 1):
        print("\n ------------------- Account login -------------------");
        account = input("Public key: ");
        os.system('clear');
        manage_account.login(account);
    elif(int(option) == 2):
        print("\n ------------------- New account -------------------");
        print("1: Create account");print("2: Sign and validate account");
        n_option = input("Choose an option: ");
        if (int(n_option) == 1):
            os.system('clear');
            create_account.createAccount();
        elif (int(n_option) == 2):
            os.system('clear');
            print("\n ------------------- Sign and validate account -------------------");
            print("\nAdd your address and private key");
            print("You could find them in the '01_Account_Info.txt' file");
            print("\nWARNING: Never let anyone to have your private key\n");
            print("You may need some Ether to do the transaction");
            address = input("\nAddress of new created account: ");
            private_key = input("Private key of new account: ");
            create_account.transactionAccount(address, private_key, web3);
        else:
            print("Invalid option");
    elif(int(option) == 3):
        os.system('clear');
        explore_blocks.exploreBlocks(web3);


#Calling main function
main();


# Faculty of Mathematics at Merida, Yucatan
