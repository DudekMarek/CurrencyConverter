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

    #Sub-parser for adding currencies
    add_parser = subparsers.add_parser("add", help="Add new currency")


    args = parser.parse_args()

    if args.operations == "list":
        for item in data_handler.list_stored_currencies():
            print(item)

    elif args.operations == "add":
        currency_name = input("Enter currency name (eg. USD): ")
        currency_dollar_course = input("Enter currency course to dollar (eg. 1.4): ")

        new_currency = Currency(name=currency_name, dolar_course=currency_dollar_course)

        data_handler.add_currency(new_currency)

    # parser.add_argument("-l", "--list", help="List available currencies", action="store_true")
    # parser.add_argument("-a", "--add-currency", help="Add new currency in following format: CURRENCY_NAME:COURSE_TO_DOLLAR")
    # args = parser.parse_args()

    # if args.list:
    #     for item in data_handler.list_stored_currencies():
    #         print(item)
    #     sys.exit(0)

    # if args.add_currency:
    #     new_currency = Currency()
    #     data_handler.add_currency()

if __name__ == "__main__":
    main()