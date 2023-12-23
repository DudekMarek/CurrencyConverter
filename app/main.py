import json
import argparse
import sys

from currency import Currency
from data_store import DataHandler

def main():
    data_handler = DataHandler("test.json")

    try:
        data_handler.read_data()
    except FileNotFoundError:
        data_handler.write_data()
    

    parser = argparse.ArgumentParser(description="Simple CLI currency converter")

    # Create subparsers
    subparsers = parser.add_subparsers(dest="operations", help="Awailable operations")

    # Sub-parser for listing entities
    list_parser = subparsers.add_parser("list", help="List available currencies")

    # Sub-parser for adding currencies
    add_parser = subparsers.add_parser("add", help="Add new currency")

    # Sub-parser for currency converter
    convert_parser = subparsers.add_parser("convert", help="Convert one currency to another")
    convert_parser.add_argument("-f", "--from-currency", help="Currency that you want to convert", type=str, choices=data_handler.list_stored_currencies())
    convert_parser.add_argument("-t", "--target-currency", help="Target currency", type=str, choices=data_handler.list_stored_currencies())
    convert_parser.add_argument("-a", "--amount", help="Amount of currency to convert", type=float)


    args = parser.parse_args()

    if args.operations == "list":
        for item in data_handler.list_stored_currencies():
            print(item)

    elif args.operations == "add":
        currency_name = input("Enter currency name (eg. USD): ")
        currency_dollar_course = input("Enter currency course to dollar (eg. 1.4): ")

        new_currency = Currency(name=currency_name, dolar_course=currency_dollar_course)

        data_handler.add_currency(new_currency)

    elif args.operations == "convert":
        from_currency_name = args.from_currency
        target_currency_name = args.target_currency
        amount = args.amount
        from_currency = Currency(name=from_currency_name, dolar_course=data_handler.data[from_currency_name])
        target_currency = Currency(name=target_currency_name, dolar_course=data_handler.data[target_currency_name])

        print(from_currency.convert_to_another_currency(target_currency, amount))



if __name__ == "__main__":
    main()