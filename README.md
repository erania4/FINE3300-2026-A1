# **FINE3300-2026-Assignment One**

## Exchange Rate Calculator

This public repository is for my first assignment in my FINE3300 - Python for Finance Professionals class. The primary assignment was to create a functioning exchange rate calculator using classes in Python, that read and extract specific values from files to use in the conversion of the currencies. The secondary assignment was to have a Large Language Model (LLM) write the code for me, doing the same thing required by me in the first part of the project. 
I hope you learn from, appreciate and/or enjoy using my code. Good luck fellow coder!

# **Part One – Exchange Rates**

## Assignment Section Overview

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

User inputs are italicized.

### Exchanging $100,000 USD to CAD using BankOfCanadaExchangeRate.2026.csv:

>Please enter the amount you would like to convert (with no formatting): *100000*
>Enter the 'from' currency (USD or CAD): *USD*
>Enter the 'to' currency (USD or CAD): *CAD*
>Enter the path to the exchange rate file you would like to reference: *"C:\Users\erani\Downloads\BankOfCanadaExchangeRate.2026.csv"*
>$100,000.00 USD is equal to $139,780.00 CAD!

### Exchanging $100,000 CAD to USD using BankOfCanadaExchangeRate.2026.csv:

>Please enter the amount you would like to convert (with no formatting): *100000*
>Enter the 'from' currency (USD or CAD): *CAD*
>Enter the 'to' currency (USD or CAD): *USD*
>Enter the path to the exchange rate file you would like to reference: *"C:\Users\erani\Downloads\BankOfCanadaExchangeRate.2026.csv"*
>$100,000.00 CAD is equal to $71,540.99 USD!

# Part Two – Vibe Coding

## Assignment Section Overview

For the second part of the assignment, I was required to prompt an LLM/AI model to write code for me that fulfills the same assignment I had completed myself. In doing so, I needed to create a separate Python file, which can be found in my attached repository. Lastly, after testing the code in my Visual Studio Code environment to ensure its functionality, I had to compare the LLM’s code with my own code and make note of major differences and similarities.

## The LLM/AI Model Used

I used Claude as my AI model for the Vibe Coding part of the project. Specifically, the AI model that I used runs Claude Sonnet 5.5 on the high effort level.

## Exact Prompts Provided
Below is the prompt that I delivered in Claude AI’s “Chat” box. Keep in mind that I also attached the BankOfCanadaExchangeRate.2026.csv file.

> Claude AI. Can you please code something for me? 
> I need you to create an exchange rate calculator in Python for USD/CAD currency exchanges. First, design a class (called ExchangeRates) that takes an exchange rate file.  Use the attached file (BankOfCanadaExchangeRate.2026.csv) as an example file, but keep the code in general terms so that any user could input their own file. Next, write a method/function (defined as convert) that takes the amount and two currencies, and can convert it from one currency to another using the exchange rate read from the file. Moreover, the user must be prompted to specify the amount, the "from" currency (CAD or USD) and the "to" currency (CAD or USD) that they would like to use in the conversion. Use the input() function to help with this. Furthermore, assume legitimate entries with no need for validation and keep conversions rounded to the penny.
> The exchange rate of interest, using the attached file as a basis for the assignment, is the latest USD/CAD exchange rate. 

During my first review, I noticed that the input() functions to prompt the user didn’t appear when I ran the code. Instead, there were several errors. So, I attached a picture of the errors to the AI and reminded it of the need to prompt users. My next prompt was as follows:

>When I run the code an error appears. I have attached a screenshot of the error to this message. Furthermore, I should remind you that part of the task is to prompt the user using the input() function, which does not appear in your code. Please make the appropriate alterations to fix the code.

This next time, I noticed that everything was working much better. I found that I was properly prompted and given the correct answer when using valid inputs (amounts and currencies).

## The LLM/AI Model’s Output

User inputs are italicized.

### Exchanging $100,000 USD to CAD using BankOfCanadaExchangeRate.2026.csv:

> Enter the exchange rate file name: "C:\Users\erani\Downloads\BankOfCanadaExchangeRate.2026.csv"
>Enter the amount: *100000*
>Convert from (CAD or USD): *USD*
>Convert to (CAD or USD): *CAD*
>Latest USD/CAD rate: 1.3978
>100000.00 USD = 139780.00 CAD

### Exchanging $100,000 CAD to USD using BankOfCanadaExchangeRate.2026.csv:

>Enter the exchange rate file name: "C:\Users\erani\Downloads\BankOfCanadaExchangeRate.2026.csv"
>Enter the amount: *100000*
>Convert from (CAD or USD): *CAD*
>Convert to (CAD or USD): *USD*
>Latest USD/CAD rate: 1.3978
>100000.00 CAD = 71540.99 USD

## Code Comparison
Upon first glance, I noticed that the AI model’s code had many minor differences. This came in the form of different variable definitions, many multi-line strings and much less notes (which I only used more of to show my thoughts and explain my reasoning to my professor and users).

After deeper review of the code, I noticed more significant differences and even some major similarities. Early in the code, the LLM defined RATE_COLUMN which was used later to find the exchange rate in the file. Moreover, the AI model coded a for loop to go through the iterations in the dictionary under the FXAUSDCAD column, instead of using a list of dictionaries as I did. That is how it read through the rates of interest in the file. Furthermore, to find the latest rate, the AI model used an “if” statement to ensure that there was no blank value being used and so that when the blank value was reached, the code would identify the value that came before it as the “latest_rate” to be used in the calculations. This is much different than how I extracted the rate, but very interesting indeed. The rate was also printed later in the output code, which I thought was a nice touch. One other thing that the AI model’s code did differently was use a decimal import to round results. It also used f-strings for printed results, instead of the regular format function like my code uses. Later, however, the AI rounded the amounts in a similar fashion to my code, with the “:.2f” formatting when printing the output to users. Although, it still didn’t include my formatting for the comma at every thousand. Another similarity between our codes that I was surprised to see was that the LLM’s code also manually opened and closed the file to read it. I originally thought it would have used the “with open” method, which I believed was more common in advanced coding. Finally, to conclude with perhaps the most significant difference between our two codes, the AI model did not include any code for any invalid user inputs. Claude AI’s code solely determined what conversion calculation to use based on whether the “from” currency was “USD”. This means that if you input AUD as the “from” currency, for example, it would assume you are converting your amount from CAD to USD and return your value as such. This lacks the robustness of my code, which has prepared messages and outputs for various user input errors. The original prompt said to assume that users provide legitimate input values, so that is likely the case for the LLM’s lack of robustness, but it is nonetheless a major difference that lacks important considerations.

# External Sources Consulted

- https://docs.python.org/3/library/csv.html#csv-fmt-params
- https://www.askpython.com/python/string/python-floating-point-formatting
- https://www.w3schools.com/python/ref_string_strip.asp
- https://www.w3schools.com/python/ref_string_upper.asp
- https://www.w3schools.com/python/python_user_input.asp
- https://youtu.be/7MciGRf8V3A?si=_Pfn_PPqByAmo1lU

# Thank you! I hope you enjoyed the code and the overview!
