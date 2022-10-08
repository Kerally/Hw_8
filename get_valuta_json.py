import json


dict = json.load(open('C:/Users/User/Documents/GitHub/Converter/symbols.json', 'r', encoding='utf-8'))

valuta_list = []

for i in dict['symbols'].keys():
    valuta_list.append(i)

