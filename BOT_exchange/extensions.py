import json
import requests
from config import exchanges
from config import headers, payload

class APIException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(base, sym, amount):

        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена!")

        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        if amount <= 0:
            raise APIException(f'Количество не может быть меньше либо равно нулю')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={sym_key}&from={base_key}&amount={amount}"

        r = requests.request("GET", url, headers = headers, data = payload)
        resp = json.loads(r.content)
        new_price = resp['result']
        new_price = round(new_price, 3)
        message = f"Цена {amount} {base} в {sym} : {new_price}"
        return message