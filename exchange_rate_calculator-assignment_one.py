import csv
    # My first step, as seen above, was to import the csv (comma-separated values) module. 
    # This will allow me to properly make my way through the BankOfCanadaExchangeRate.2026.csv file and extract the required data.

class ExchangeRates:
    def __init__(self, rate_file_name):    
        # Initializes the class and defines the object.
        
        self.rate_file_name = rate_file_name
            # Set rate_file_name as a variable that represents the path to an exchange rate file.
                # Chose not to hardcode the file. The assignment asks for a class that "takes an exchange rate file" in general terms.
                # The class and object defined under it will reference the file inputted by the user later.
            # The BankOfCanadaExchangeRate.2026.csv file will be used for this assignment. Despite this, any similarly formatted exchange rate file can be used.

        open_rate_file = open(rate_file_name, "r")
            # Object opens the file.
            # Note that the file is opened in read mode, as indicated by the "r" argument.

        reader = csv.DictReader(open_rate_file)
        self.years = list(reader)
            # Defined the reader object as DictReader (as opposed to an ordinary reader) to read the file and access its values as a dictionary.
            # Converted the reader object into a list (of dictionaries) defined as years, because the list will split the dictionaries (of rates and currencies) by year.
        
        open_rate_file.close()
            # Closes the file after it has been read.

        self.exchange_rate = float(self.years[-1]["FXAUSDCAD"])
            # The code above accesses and defines the USD to CAD exchange rate from the file. The rate is $1.3978 USD/CAD from the assigned file.
            # Turning it into a float is necessary for arithmetic operations. Otherwise, it would have been a string.
                # The [-1] index accesses the last dictionary in the list, ensuring that the code always takes the rate from the most recent year. 
                # "FXAUSDCAD" acts as a key to access the value of the USD to CAD exchange rate in that dictionary.


    # Below I defined the convert method. This method will take in the amount to be converted, the currency to convert from, and the currency to convert to.
    # The method will use the exchange rate from the inputted file.

    def convert (self, amount, from_currency, to_currency):
        if amount < 0:
            print ("The amount to be converted is negative. This is invalid. Please try again with a positive amount.")
                # This ensures that the amount being converted is greater than or equal to zero (not negative).
                # By coming first, the negative amount is not passed over before being considered.

            if from_currency not in ("CAD", "USD") or to_currency not in ("CAD", "USD"):
                print ("Moreover, the from currency and/or the to currency are also invalid. The only valid currencies are CAD and USD. Ensure you are using these currencies and try again.")
                    # The nested "if" statement provides an additional message for users who have also inputted an invalid currency.
            return None
        
        elif from_currency == "USD" and to_currency == "CAD":
            usd_to_cad = amount * self.exchange_rate
            print ("${:,.2f} USD is equal to ${:,.2f} CAD!".format(amount, usd_to_cad))
            return usd_to_cad

        elif from_currency == "CAD" and to_currency == "USD":
            cad_to_usd = amount / self.exchange_rate
            print ("${:,.2f} CAD is equal to ${:,.2f} USD!".format(amount, cad_to_usd))
            return cad_to_usd

            # The "elif" statements above provide a specific message to the user with their desired output.
            # Formatting is used to round the currencies to the nearest hundredth (or cent), and to input commas for every thousand.
            # Format inputs the corresponding values into the resulting print statement.

        elif from_currency == "USD" and to_currency == "USD":
            print ("The from currency and the to currency are the same (both USD). No conversion takes place.")
            return amount

        elif from_currency == "CAD" and to_currency == "CAD":
            print ("The from currency and the to currency are the same (both CAD). No conversion takes place.")
            return amount

            # A message prints for the user if the two currencies entered are the same. 
            # By separating the "elif" statement into two, the user will be notified as to which currency appears twice.

        else:
            print ("The from currency and/or the to currency are not valid. The only convertible currencies are CAD and USD. Please try again using these currencies.")
            return None

            # If one of the two currencies is not CAD or USD, this statement is printed informing the user of their invalidity.

amount = float(input("Please enter the amount you would like to convert: "))
from_currency = input("Enter the 'from' currency (USD or CAD): ").strip().upper()
to_currency = input("Enter the 'to' currency (USD or CAD): ").strip().upper()
exchange_rate_file = input("Enter the path to the exchange rate file you would like to reference: ").strip().strip('"')
    # This prompts the user to input their similarly formatted exchange rate file, the amount and the currencies for the conversion.
    # "Strip" eliminates quotation marks and spaces from before and after inputs. "Upper" converts currency entries to uppercase.

exchange = ExchangeRates(exchange_rate_file)
convert_currency = exchange.convert(amount, from_currency, to_currency)
    # Entries from the user's inputs are sent here, where the class and method get called to action and execute.