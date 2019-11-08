#--------------------------------------------------------------------------
# NASA/GSFC, Software Integration & Visualization Office, Code 610.3
#--------------------------------------------------------------------------
#
# MODULE: Mini blockchain project || Account management
# FILE: manage_account.py
# USE: python3 blockchain.py || This script is called by "blockchain.py"
#
#> @author
#> Albert Aaron Cervera Uribe
#
#  DESCRIPTION:
#> This script allow retrieval of information associated within accounts
#
# REVISION HISTORY:
#
# 05 November 2019 - Initial Version
# 07 November 2019 - Final Version
#
# MODIFICATIONS:
#
# Initial mod. version: --------
# Final mod. version:   --------
#
# TODO_dd_mmm_yyyy - TODO_describe_appropriate_changes - TODO_name
#--------------------------------------------------------------------------
import etherscan;
import transferValue as transfer;
import os;

#Public key to test: 0x140427a7D27144A4cDa83bD6b9052a63b0c5B589

es = etherscan.Client(
    api_key='https://ropsten.infura.io/v3/963aa3c429b5444cb0e007241f8bf0fd',
    cache_expire_after=5,
)

"""
Function: login
Input: account (a public address)
Returns: --
Description: It presents the balance of an account as well as allowing users to
explore transactions associated within the account or to make transactions of
Ether or Tokens
"""
def login(account):
    print("\n ---------------- Account login ----------------");
    print("Account: " + account);
    balance = es.get_eth_balance(account);
    print("\nBalance in wei: " + str(balance));
    print("Balance in Ether: " + str(balance/(10**18)));
    print("Transactions made: " + str(len(es.get_transactions_by_address(account))));
    print("\n");
    print("1) See transactions");
    print("2) Transfer Ether or Tokens");
    print("3) Leave session");
    option = input("Choose an option: ");
    if (int(option) == 1):
        getTransactions(account);
    elif(int(option)==2):
        os.system('clear');
        transfer.transferMain(account);
    elif(int(option)==3):
        print("\nThanks for using Blockchain!");
    else:
        print("\nInvalid input");


"""
Function: getTransactions
Input: account (a public address)
Returns: --
Description: Resumes the last 5 transactions associated with an account
"""
def getTransactions(account):
    labels = ['timestamp', 'block_number','from','to','input','hash','value','gas','gas_price','gas_used','nonce','confirmations','is_error','tx_receipt_status','transaction_index','cumulative_gas_used','block_hash'];
    print("\nTransactions -------------------------------------------------\n");
    transactions = es.get_transactions_by_address(account);
    print("Length of available transactions: " + str(len(transactions)));

    input("\nPress enter to see the last 5 transactions associated with this account/contract:\n");
    for i in range(5):
        if (i < len(transactions)):
            print("\n\n\nTransaction number: " + str(i) + ":");
            for j in range(len(labels)):
                print(str(labels[j]) + ": " + str(transactions[(len(transactions)-1)-i][labels[j]]));
        elif(i >= len(transactions)):
            print("\n\n"+ str(i) +") " + "N/A");

    print("");
    input("\nPress enter continue");
    print("\nTransactions -------------------------------------------------\n");
    print("1) Filter transactions");
    print("2) Return");
    option = input("Choose an option: ");
    if (int(option)== 1):
        os.system('clear');
        filterTransactions(account);
    elif (int(option) == 2):
        os.system('clear');
        login(account);


"""
Function: filterTransactions
Input: account (a public address)
Returns: --
Description: Enables users to choose a criteria filter for transaction filtering
"""
def filterTransactions(account):
    print("\nFilter Transactions ------------------------------------------\n");
    print("You can filter the last 5 transactions by a criteria:\n");
    print("01) input");
    print("02) hash");
    print("03) value");
    print("04) gas");
    print("05) gas_price");
    print("06) gas_used");
    print("07) nonce");
    print("08) confirmations");
    print("09) is_error");
    print("10) tx_receipt_status");
    print("11) transaction_index");
    print("12) cumulative_gas_used");
    print("13) block_hash");

    option = input("\nChoose an option: ");
    os.system('clear');
    if (int(option) == 1):
        label = 'input';
        filter(account,label);
    elif (int(option)== 2):
        label = 'hash';
        filter(account,label);
    elif (int(option)== 3):
        label = 'value';
        filter(account,label);
    elif (int(option)== 4):
        label = 'gas';
        filter(account,label);
    elif (int(option)== 5):
        label = 'gas_price';
        filter(account,label);
    elif (int(option)== 6):
        label = 'gas_used';
        filter(account,label);
    elif (int(option)== 7):
        label = 'nonce';
        filter(account,label);
    elif (int(option)== 8):
        label = 'confirmations';
        filter(account,label);
    elif (int(option)== 9):
        label = 'is_error';
        filter(account,label);
    elif (int(option)== 10):
        label = 'tx_receipt_status';
        filter(account,label);
    elif (int(option)== 11):
        label = 'transaction_index';
        filter(account,label);
    elif (int(option)== 12):
        label = 'cumulative_gas_used';
        filter(account,label);
    elif (int(option)== 13):
        label = 'block_hash';
        filter(account,label);
    else:
        print("\nError choosing option");


"""
Function: filter
Input: account (a public address), label (string of criteria filter)
Returns: --
Description: It filters a transaction by its given criteria filter.
"""
def filter(account, label):
    print("\nFilter Transactions ------------------------------------------\n");
    print("Filtering by: " + str(label) + "\n");
    transactions = es.get_transactions_by_address(account);

    for i in range(5):
        if (i < len(transactions)):
            print("\n\nTransaction number: " + str(i) + ":");
            print("block_number: " + str(transactions[(len(transactions)-1)-i]['block_number']));
            print("from: " + str(transactions[(len(transactions)-1)-i]['from']));
            print("to: " + str(transactions[(len(transactions)-1)-i]['to']));
            print(str(label) + ": " + str(transactions[(len(transactions)-1)-i][label]));
        elif(i >= len(transactions)):
            print("\n\n"+ str(i) +") " + "N/A");

    input("\nPress enter continue");
    print("\nFilter Transactions ------------------------------------------\n");
    print("1) Return to filter criteria");
    print("2) Return to account");
    option = input("Choose an option: ");
    if (int(option)== 1):
        os.system('clear');
        filterTransactions(account);
    elif (int(option) == 2):
        os.system('clear');
        login(account);


# Faculty of Mathematics at Merida, Yucatan
