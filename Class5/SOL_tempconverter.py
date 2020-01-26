# OMIS 30
# author: mdavis
# Temperature Converter Solution

'''
Create a script named 'tempconverter.py'.
It should have three lines:
1) Define a starting temperature in Fahrenheit.  For this exercise, start with 35.  Save it as a variable F.
2) A formula converting the Fahrenheit degrees to Celsius degrees, rounded to two decimal places.  Save that as C.
3) A statement that prints "<F> degrees in Fahrenheit is equivalent to <C> degrees in Celsius."

Make sure you round!  Google 'python round to two decimal places' if you're not sure how to do it!
Remember to replace the <F> with the actual starting temperature.  Use the variable name rather than the hard-coding the 35 degrees.
Attention to detail - make sure that you're using the correct words and punctuation in the print statement!
'''

F = 35
C = round((F - 32) * (5/9), 2)
print(str(F) + " degrees in Fahrenheit is equivalent to " + str(C) + " degrees in Celsius.")

# Python3 also has these cool things called f-strings.
# They're neat because they don't make you do these str() conversions
# Notice the {} notation, plus the 'f' in front of the string
print(f"{F} degrees in Fahrenheit is equivalent to {C} degrees in Celsius.")