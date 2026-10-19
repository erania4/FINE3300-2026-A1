"""USD/CAD exchange rate calculator.

Reads a Bank of Canada style exchange rate CSV file, picks out the latest
USD/CAD rate, and converts an amount between USD and CAD.
"""

import csv
import os
from decimal import Decimal, ROUND_HALF_UP


class ExchangeRates:
    """Holds the latest USD/CAD exchange rate read from a CSV file."""

    # Column in the Bank of Canada file that holds the USD/CAD rate.
    # The rate means: how many CAD are needed to buy 1 USD.
    RATE_COLUMN = "FXAUSDCAD"

    def __init__(self, file_name):
        """Locate the rate file and read the latest USD/CAD rate from it."""
        self.file_name = self._locate_file(file_name)
        self.rate = self._read_latest_rate()

    def _locate_file(self, file_name):
        """Return a usable path for the file.

        Looks in the current folder first, then in the folder that holds
        this script, so the program works wherever it is run from.
        """
        if os.path.exists(file_name):
            return file_name

        script_folder = os.path.dirname(os.path.abspath(__file__))
        script_folder_path = os.path.join(script_folder, file_name)
        if os.path.exists(script_folder_path):
            return script_folder_path

        return file_name  # let open() report the problem if it is missing

    def _read_latest_rate(self):
        """Return the last non-empty USD/CAD rate in the file as a Decimal."""
        # utf-8-sig quietly removes the BOM that Bank of Canada files start with
        file = open(self.file_name, newline="", encoding="utf-8-sig")
        reader = csv.DictReader(file)

        latest_rate = None
        for row in reader:
            value = row[self.RATE_COLUMN].strip()
            # Rows are in date order, so the last filled-in value is the latest
            if value != "":
                latest_rate = value

        file.close()
        return Decimal(latest_rate)

    def get_rate(self):
        """Return the latest USD/CAD rate (CAD per 1 USD)."""
        return self.rate

    def convert(self, amount, from_currency, to_currency):
        """Convert amount from one currency (CAD or USD) to the other.

        The result is rounded to the nearest penny.
        """
        amount = Decimal(str(amount))
        from_currency = from_currency.strip().upper()
        to_currency = to_currency.strip().upper()

        if from_currency == to_currency:
            result = amount                  # nothing to convert
        elif from_currency == "USD":
            result = amount * self.rate      # USD -> CAD
        else:
            result = amount / self.rate      # CAD -> USD

        return result.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def main():
    """Prompt the user for the file and the conversion, then print the result."""
    # Ask for the file name (e.g. BankOfCanadaExchangeRate_2026.csv)
    file_name = input("Enter the exchange rate file name: ").strip().strip('"')
    rates = ExchangeRates(file_name)

    # Ask for the conversion details
    amount = input("Enter the amount: ")
    from_currency = input("Convert from (CAD or USD): ")
    to_currency = input("Convert to (CAD or USD): ")

    result = rates.convert(amount, from_currency, to_currency)

    print(f"Latest USD/CAD rate: {rates.get_rate()}")
    print(f"{Decimal(amount):.2f} {from_currency.strip().upper()} = "
          f"{result} {to_currency.strip().upper()}")


if __name__ == "__main__":
    main()