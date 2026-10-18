# FINE3300-2026-Assignment One
## Exchange Rate Calculator
This public repository is for my first assignment in my FINE3300 - Python for Finance Professionals class. The primary assignment was to create a functioning exchange rate calculator using classes in Python, that read and extract specific values from files to use in the conversion of the currencies. The secondary assignment was to have a Large Language Model (LLM) write the code for me, doing the same thing required by me in the first part of the project. 
I hope you learn from, appreciate and/or enjoy using my code. Good luck fellow coder!

## Part One – Exchange Rates
### Design a Class
For this assignment, I was instructed to design a class (named ExchangeRates) that could read and use exchange rates found within a file. I was provided a CSV (comma-separated values) file to use in my code construction. This file contained the exchange rate of interest, which was the 01-01-2025 USD to CAD exchange rate. However, the class was to be coded so that it could take any similarly formatted file inputted by the user, and run the same code/calculations with that file’s data.
### Construct a Method
Inside of the class, a method (defined as convert) needed to be written that could take any amount and two currencies (CAD and USD in either order) and convert one currency to another using the rate found in the file. Moreover, the user must have been prompted to specify the amount, the “from” currency and the “to” currency using Python’s input() function.
### Convert the Currency
The desired result, upon running the code, is that the user inputs their desired amount, “from” currency and “to” currency, which will be converted from one to the other using the exchange rate that it read in the exchange rate file that is provided (or will be provided by the user).
## My GitHub Repository
My completed code, which is prepared to be used for exchange rate conversions, can be found in my repository. Below, I have chosen to attach my GitHub repository using the following link:
https://github.com/erania4/FINE3300-2026-A1.git
## My Code’s Output
Upon running my code, and providing the inputs when prompted, the following output is given:
###Exchanging $100,000 USD to CAD using BankOfCanadaExchange.2026.csv:
Please enter the amount you would like to convert (with no formatting): 100000
Enter the 'from' currency (USD or CAD): USD
Enter the 'to' currency (USD or CAD): CAD
Enter the path to the exchange rate file you would like to reference: "C:\Users\erani\Downloads\BankOfCanadaExchangeRate.2026.csv"
$100,000.00 USD is equal to $139,780.00 CAD!
###Exchanging $100,000 CAD to USD using BankOfCanadaExchange.2026.csv:
Please enter the amount you would like to convert (with no formatting): 100000
Enter the 'from' currency (USD or CAD): CAD
Enter the 'to' currency (USD or CAD): USD
Enter the path to the exchange rate file you would like to reference: "C:\Users\erani\Downloads\BankOfCanadaExchangeRate.2026.csv"
$100,000.00 CAD is equal to $71,540.99 USD!

## Part Two – Vibe Coding
### Assignment Section Overview
For the second part of the assignment, I was required to prompt an LLM/AI model to write code for me that fulfills the same assignment I had completed myself. In doing so, I needed to create a separate Python file, which can be found in my attached repository. Lastly, after testing the code in my Visual Studio Code environment to ensure its functionality, I had to compare the LLM’s code with my own code and make note of major differences and similarities.
### The LLM/AI Model Used

### Exact Prompts Provided

### The LLM/AI Model’s Output

### Code Comparison
