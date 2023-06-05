
from src.scroll_state import ScrollState


if __name__ == '__main__':
    address = "0x34FED72c7fA60ab0da7070c06Dd1DaD5d8B889Fb"
    ss = ScrollState(address=address)
    number_tx_success = ss.number_tx_success()
    print(f"Number of tx success: {number_tx_success}")
    deposit = ss.deposit()
    print(f"Bridge deposit : {deposit} ETH")
    withdraw = round(ss.withdraw(), 2)
    print(f"Bridge withdraw: {withdraw} ETH")
