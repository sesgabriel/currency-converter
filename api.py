import requests
from config import base_url

def get_exchange_rate(from_currency, to_currency):
    url = f"{base_url}/{from_currency}-{to_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        chave_api = f'{from_currency}{to_currency}'

        rate = float(data[chave_api]['bid'])
        return rate
    
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print("Invalid currency code.")
    return None

