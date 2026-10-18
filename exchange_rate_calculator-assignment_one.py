import csv
    # My first step, as seen above, was to import the csv (comma-separated values) module. 
    # This will allow me to properly make my way through the BankOfCanadaExchangeRate.2026.csv file and extract the required data.

class ExchangeRates:
    def __init__(self, rate_file_name):    
        # Initialize the class and define the object.
        self.__rate_file_name = rate_file_name
            # Here, I set rate_file_name as a variable that represents the path to an exchange rate file.
                # I chose not to set the assigned file as the default file path for the object, because the assignment asks for a class that "takes an exchange rate file" in general terms.
            # By doing this, the class and object defined under it will reference the file inputted by the user later.
                # I will be using the BankOfCanadaExchangeRate.2026.csv file for this assignment. Despite this, any similarly formatted exchange rate file can be used.

        self.open_rate_file = open(rate_file_name, "r")
            # This object opens the file. I defined the object as open_rate_file for that reason.
            # Note that the file is opened in read mode, as indicated by the "r" argument.

        reader = csv.DictReader(self.open_rate_file)
        self.years = list(reader)
            # Defining the reader object as a DictReader (as opposed to an ordinary reader) allows me to read the file and access its values as a dictionary.
            # Next, I converted the reader object into a list (of dictionaries). I defined it as years because the list will split the dictionaries (of rates and currencies) by year.

        self.exchange_rate = float(self.years[-1]["FXAUSDCAD"])
            # The code above accesses and defines the USD to CAD exchange rate from the file. The rate is $1.3978 USD/CAD from the assigned file.
                # Turning it into a float is necessary for arithmetic operations. Otherwise, it would have been a string.
                # The [-1] index accesses the last dictionary in the list, which is the most recent year. If the file were to be updated to more recent years, the code would still work because it would always access the last dictionary (latest year) in the list.
                # "FXAUSDCAD" acts as a key to access the value of the USD to CAD exchange rate in that dictionary.


    # Below I defined the convert method. This function will take in the amount to be converted, the currency to convert from, and the currency to convert to.
    # The function will use the exchange rate from the inputted file to convert the amount accross the two currencies.
        # Depending on the amount being converted, the "from" currency and the "to" currency, a different message will be printed upon execution of the code.

    def convert (self, amount, from_currency, to_currency):
        if amount < 0:
            print ("The amount to be converted is negative. This is invalid. Please try again with a positive amount.")

            if from_currency not in ("CAD", "USD") or to_currency not in ("CAD", "USD"):
                print ("Moreover, the from currency and/or the to currency are also invalid. The only valid currencies are CAD and USD. Ensure you are using these currencies and try again.")

            # This if statement is used to ensure that the amount being converted is greater than or equal to zero (not negative).
            # Note that this statement is first because it is the only one that relates to amount. If it came afterward, it would be passed over without being considered.
                # The nested "if" statement provides an additional message for users who have inputted a negative amount and an invalid currency.
        

        elif from_currency == "USD" and to_currency == "CAD":
            usd_to_cad = amount * self.exchange_rate
            print ("${:,.2f} USD is equal to ${:,.2f} CAD!".format(amount, usd_to_cad))
            return usd_to_cad

        elif from_currency == "CAD" and to_currency == "USD":
            cad_to_usd = amount / self.exchange_rate
            print ("${:,.2f} CAD is equal to ${:,.2f} USD!".format(amount, cad_to_usd))
            return cad_to_usd

            # These elif statements above provide a specific message to the user with their output, based on their desired conversion.
            # Formatting is used to round the currencies to the nearest hundredth (or cent), and to input commas for every thousand.
            # Format inputs the corresponding values into the resulting print statement.


        elif from_currency == "USD" and to_currency == "USD":
            print ("The from currency and the to currency are the same (both USD). No conversion takes place.")
            return amount

        elif from_currency == "CAD" and to_currency == "CAD":
            print ("The from currency and the to currency are the same (both CAD). No conversion takes place.")
            return amount

            # If the two currencies entered are the same, the following elif statements print a message to inform the user of such.

        else:
            print ("The from currency and/or the to currency are not valid. The only convertible currencies are CAD and USD. Please try again using these currencies.")

        # If one of the two currencies is not CAD or USD, this statement is printed informing the user of their invalidity.


exchange_rate_file = ExchangeRates("C:/Users/erani/Downloads/BankOfCanadaExchangeRate.2026.csv")
currency_exchange = exchange_rate_file.convert(-10000, "USD", "CAD")

amount = float(input("Amount to be converted: "))
from_currency = input("From currency (USD or CAD): ")
to_currency = input("To currency (USD or CAD): ")
exchange_rate_file = input("Enter the path to the exchange rate file you would like to reference: ")

# need to fix these inputs or at least make sure they work/do their job
# need to close file and so I might need to switch to the "with" file reader