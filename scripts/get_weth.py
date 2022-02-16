from scripts.helpful_scripts import get_account
from brownie import interface, network, config, accounts
from web3 import Web3
import sys

amount = Web3.toWei(0.1, "ether")


def get_weth():
    account = get_account()  # add your keystore ID as an argument to this call
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": amount})
    tx.wait(1)
    print("Received 0.1 WETH")
    return tx


def main():
    get_weth()
