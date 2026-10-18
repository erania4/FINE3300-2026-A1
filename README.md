# FINE3300-2026-Assignment One
## Exchange Rate Calculator
This public repository is for my first assignment in my FINE3300 - Python for Finance Professionals class. The primary assignment was to create a functioning exchange rate calculator using classes in Python, that read and extract specific values from files to use in the conversion of the currencies. I hope you learn from, appreciate and/or enjoy using my code. Good luck fellow coder!

## Detailed Assignment Overview
For this assignment, I was instructed to design a class (named ExchangeRates) that could read and use exchange rates found within a file. I was provided a CSV (comma-separated values) file to use in my code construction. This file contained the exchange rate of interest, which was the 01-01-2025 USD to CAD exchange rate. However, the class was to be coded so that it could take any similarly formatted file inputted by the user, and run the same code/calculations with that file’s data.

Inside of the class, a method (defined as convert) needed to be written that could take any amount and two currencies (CAD and USD in either order) and convert one currency to another using the rate found in the file. Moreover, the user must have been prompted to specify the amount, the “from” currency and the “to” currency using Python’s input() function.

The desired result, upon running the code, is that the user inputs their desired amount, “from” currency and “to” currency, which will be converted from one to the other using the exchange rate that it read in the exchange rate file that is provided (or will be provided by the user).
