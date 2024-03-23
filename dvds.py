import requests
from bs4 import BeautifulSoup

def get_usd_exchange_rate():
    url = 'https://www.google.com/search?q=usd+to+uah'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    exchange_rate = soup.find('span', class_='DFlfde SwHCTb').text
    return float(exchange_rate)
usd_rate = get_usd_exchange_rate()
print(f'Курс долара США: {usd_rate}')
class CurrencyConverter:
    def __init__(self, usd_rate):
        self.usd_rate = usd_rate
    def convert_to_usd(self, amount):
        return amount / self.usd_rate
usd_rate = get_usd_exchange_rate()
converter = CurrencyConverter(usd_rate)
amount = float(input('Введіть кількість вашої валюти: '))
usd_amount = converter.convert_to_usd(amount)
print(f'{amount} у вашій валюті дорівнює {usd_amount} доларам США')
