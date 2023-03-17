import requests
import datetime
from json.decoder import JSONDecodeError


def get_exchange_rates():
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json1212'
    response = requests.get(url)
    try:
        data = response.json()
    except JSONDecodeError:  # in this case we can use JSONDecodeError if the response is not a valid JSON
        raise ValueError('Invalid JSON response')

    with open('exchange_rates.txt', 'w') as file:  # open the file for write
        date_creation = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # write date of creation of the request
        file.write(f'[{date_creation}]\n')

        for currency in data:  # write the exchange rate of each currency
            name = currency.get('cc')
            rate = currency.get('rate')
            file.write(f'{name} to UAH: {rate}\n')


get_exchange_rates()
