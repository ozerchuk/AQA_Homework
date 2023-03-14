import requests
import datetime


def get_exchange_rates():
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json1212'
    response = requests.get(url)
    data = response.json()  # unpack JSON

    if response.status_code != 200:
        raise ValueError(f'Problem to get the exchange rate from NBU. Status code: {response.status_code}')

    with open('exchange_rates.txt', 'w') as file:  # open the file for write
        date_creation = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # write date of creation of the request
        file.write(f'[{date_creation}]\n')

        for currency in data:  # write the exchange rate of each currency
            name = currency['cc']
            rate = currency['rate']
            file.write(f'{name} to UAH: {rate}\n')


get_exchange_rates()