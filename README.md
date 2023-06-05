# py-scroll-state
Scroll Network state script support for incentive program

## Install package
```sh
pip3 install -r requirements.txt
```
or using pipenv
```sh
pipenv sync
```

## Usage
<details>
  <summary>📚 Click to see some basic examples</summary>

```python3
from src.scroll_state import ScrollState
address = "0x34FED72c7fA60ab0da7070c06Dd1DaD5d8B889Fb"
ss = ScrollState(address=address)
number_tx_success = ss.number_tx_success()
print(f"Number of tx success: {number_tx_success}")
deposit = ss.deposit()
print(f"Bridge deposit : {deposit} ETH")
withdraw = round(ss.withdraw(), 2)
print(f"Bridge withdraw: {withdraw} ETH")
```

Result dict

```python3
Number of tx success: 7
Bridge deposit : 0.14 ETH
Bridge withdraw: 0.0 ETH
```

</details>

## Contact

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/bxdoan)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/bxdoan)
[![Email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:hi@bxdoan.com)

## Thanks for use
Buy me a coffee

[![buymecoffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/bxdoan)
[![bxdoan.eth](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white)](https://etherscan.io/address/0x610322AeF748238C52E920a15Dd9A8845C9c0318)
[![paypal](	https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/bxdoan)
