import requests
import get_valuta_json
from get_date import date
get_valuta_json.valuta_list


currency_from = input("Enter the currency from: ")
currency_to = input("Enter the currency to: ")
if currency_from not in get_valuta_json.valuta_list:
    currency_from = 'USD'
if currency_to not in get_valuta_json.valuta_list:
    currency_to = 'UAH'

end_date = date[0]
start_date = date[1]

url = 'https://api.exchangerate.host/timeseries?base={0}&start_date={1}&end_date={2}&symbols={3}'.format(currency_from,start_date,end_date,currency_to)
response = requests.get(url)
data = response.json()

# заполяем масив днями с периода заданого дня и до последнего заданого
list_of_days = []
for i in data['rates'].keys():
    list_of_days.append(i)

# получаем масив с курсом валют на заданом промежутке временни
list_of_exchange_rates = []
for i in list_of_days:
    list_of_exchange_rates.append(data['rates'][i][currency_to])

# заполняем масив округлёнными значениями после перевода
list_of_amount = []
amount = input("Enter the amount: ")
if amount.isdigit() ==  False:
    amount = 100
for i in list_of_exchange_rates:
    list_of_amount.append(round(int(amount) * i, 2))


print('date', 'from', 'to', 'amount', 'rate', 'result')
for i, j, item in zip(list_of_days, list_of_exchange_rates, list_of_amount):
    print(i, currency_from, currency_to, amount, j, item)

