from api import get_exchange_rate
from calculus import convert_currency
from calculus import format_currency
from time import sleep

def menu():
    while True:
        print('CURRENCY EXCHANGE FROM KENYO')
        try:
            user_coin = str(input('type the coin you want to exchange or type quit/exit (ex: USD): ')).upper().strip()
            if user_coin == 'QUIT' or user_coin == 'EXIT':
                print('goodbye!')
                sleep(3)
                break
            if not user_coin:
                print('please, type the coin.')
                continue
            elif user_coin.isnumeric():
                print('please, only letters.')
                continue

            user_exchange = str(input('type the destination coin (ex: BRL): ')).upper().strip()
            if not user_exchange:
                print('please, type the destination coin.')
                continue
            elif user_exchange.isnumeric():
                print('please, only letters.')
                continue
            elif user_exchange == user_coin:
                print('you cannot exchange the same coin.')
                continue 
        except KeyError:
            print('please, only letters.')
            continue

        try:    
            user_amount = float(input('type the amount you want to exchange: '))
            if user_amount <= 0:
                print('please, type a positive number.')
                continue
        except ValueError:
            print('please, type a number.')
            continue
    
        rate = get_exchange_rate(user_coin, user_exchange)
        if rate is not None:
            result = convert_currency(user_amount, rate)
            print(f'You can exchange {format_currency(user_amount, user_coin)} for {format_currency(result, user_exchange)}')
            sleep(3)
        else:
            print('we did not find the exchange rate.')
            continue
            

if __name__ == '__main__':
    menu()