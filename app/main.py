import json
import argparse
import sys

from currency import Currency
from data_store import DataHandler

def main():
    data_handler = DataHandler("test")
    data_handler.read_data()

    parser = argparse.ArgumentParser(description="Simple CLI currency converter")

    parser.add_argument("-l", "--list", help="List available currencies", action="store_true")
    parser.add_argument("-a", "--add-currency", help="Add new currency in following format: CURRENCY_NAME:COURSE_TO_DOLLAR")
    args = parser.parse_args()

    if args.list:
        print(data_handler.list_stored_currencies())
        sys.exit(0)


if __name__ == "__main__":
    main()