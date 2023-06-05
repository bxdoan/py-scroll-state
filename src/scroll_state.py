import requests

API = 'https://blockscout.scroll.io/api'
L2_DEPO_ADDRESS = '0x32139b5c8838e94ffcd83e60dff95daa7f0ba14c'
L2_WITH_ADDRESS = '0x6d79Aa2e4Fbf80CF8543Ad97e294861853fb0649'


class ScrollState(object):
    def __init__(self, address, **kwargs):
        self.address = address

        if not self.address:
            raise ValueError('address is required')

        self._tx_list_external = self.tx_list_external()
        self._tx_list_internal = self.tx_list_internal()

    def tx_list_external(self):
        url = f'{API}?module=account&action=txlist&address={self.address}'
        response = requests.get(url)
        return response.json().get('result', [])

    def tx_list_internal(self):
        url = f'{API}?module=account&action=txlistinternal&address={self.address}'
        response = requests.get(url)
        return response.json().get('result', [])

    def number_tx_success(self):
        number_tx_success = len([tx for tx in self._tx_list_external if tx.get('txreceipt_status') == '1'])
        return number_tx_success + 1

    def deposit(self):
        volume = 0
        for tx in self._tx_list_internal:
            if tx.get('from').lower() == L2_DEPO_ADDRESS.lower():
                volume += int(tx.get('value'))
        volume_in_eth = volume / 10 ** 18
        return volume_in_eth

    def withdraw(self):
        volume = 0
        for tx in self._tx_list_external:
            if tx.get('to').lower() == L2_WITH_ADDRESS.lower():
                volume += int(tx.get('value'))
        volume_in_eth = volume / 10 ** 18
        return volume_in_eth

    def volume(self):
        volume = 0
        for tx in self._tx_list_external:
            if tx.get('txreceipt_status') == '1' and tx.get('value'):
                volume += int(tx.get('value'))
        for tx in self._tx_list_internal:
            if tx.get('value'):
                volume += int(tx.get('value'))

        volume_in_eth = volume / 10 ** 18
        return volume_in_eth

    def gas_used(self):
        gas_used = 0
        for tx in self._tx_list_external:
            if tx.get('gasUsed'):
                gas_used += int(tx.get('gasUsed'))
        gas_used_in_eth = gas_used / 10 ** 18
        return gas_used_in_eth
