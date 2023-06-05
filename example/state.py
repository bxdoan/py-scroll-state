
from src.scroll_state import ScrollState


if __name__ == '__main__':
    address = "0x34FED72c7fA60ab0da7070c06Dd1DaD5d8B889Fb"
    ss = ScrollState(address=address)
    print(f"Number of tx        : {len(ss.tx_list_external())}")
    print(f"Number of tx success: {ss.number_tx_success()}")
    deposit = ss.deposit()
    print(f"Bridge deposit : {deposit} ETH")
    withdraw = round(ss.withdraw(), 2)
    print(f"Bridge withdraw: {withdraw} ETH")
    volume = round(ss.volume(), 2)
    print(f"Total volume   : {volume} ETH")
    print(f"Total gas used : {ss.gas_used()} ETH")
