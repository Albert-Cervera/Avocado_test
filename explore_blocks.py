#--------------------------------------------------------------------------
# NASA/GSFC, Software Integration & Visualization Office, Code 610.3
#--------------------------------------------------------------------------
#
# MODULE: Mini blockchain project || Blocks exploration
# FILE: explore_blocks.py
# USE: python3 blockchain.py || This script is called by "blockchain.py"
#
#> @author
#> Albert Aaron Cervera Uribe
#
#  DESCRIPTION:
#> This script will help in the exploration of new blocks added to a blockchain
#
# REVISION HISTORY:
#
# 07 November 2019 - Initial Version
# 07 November 2019 - Final Version
#
# MODIFICATIONS:
#
# Initial mod. version: --------
# Final mod. version:   --------
#
# TODO_dd_mmm_yyyy - TODO_describe_appropriate_changes - TODO_name
#--------------------------------------------------------------------------
from web3 import Web3;
import os;

"""
Function: exploreBlocks
Input: web3 (the infura_url as provider from web3py)
Returns: --
Description: It enables exploration of the latest 10 blocks created within
a blockchain. Then, it allows the user to filter (or to explore) a block given
its block number.
"""
def exploreBlocks(web3):
    print("\n ---------------- Explore blocks ----------------\n");
    print("Assert web3 connection: " + str(web3.isConnected()));
    print("Block number of web3: " + str(web3.eth.blockNumber) + "\n");
    print("The latest 10 blocks numbers are: ");

    latest = web3.eth.blockNumber;
    for i in range(0, 10):
        print(str(i) + ") "+ str(web3.eth.getBlock(latest - i)['number']));

    print("\n1) Explore block by number  ||  2) Return");
    option = input("\nChoose an option: ");
    if (int(option) == 1):
        number = input("Write number of the block to explore: ");
        block = web3.eth.getBlock(int(number));
        printBlock(block);
        input("Press enter to continue");
        exploreBlocks(web3);
    elif (int(option) == 2):
        import blockchain;
        os.system('clear');
        blockchain.main();


"""
Function: printBlock
Input: a block identity from the blockchain
Returns: --
Description: Prints the attributes of a given block.
"""
def printBlock(block):
    blockLabels =  ['difficulty','extraData','gasLimit', 'gasUsed','hash','logsBloom','miner','mixHash','nonce','number','parentHash','receiptsRoot','sha3Uncles','size','stateRoot','timestamp','totalDifficulty','transactions','transactionsRoot','uncles'];
    for i in range(len(blockLabels)):
        print(str(blockLabels[i]) + ": "+ str(block[blockLabels[i]]) + "\n\n" );



# Faculty of Mathematics at Merida, Yucatan
