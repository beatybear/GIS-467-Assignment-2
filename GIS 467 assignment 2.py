# -*- coding: utf-8 -*-
"""
** All questions that take numbers as input should accept floats and integers **
1. Convert Fahrenheit to Celsius
    Write a script that prompts the user for a temperature in Fahrenheit and displays the temperature in Celsius with some message like: 
	“77.0 degrees F equals 25.0 degrees C”
2. Area of a circle
    Write a script that prompts the user for a circle’s radius and calculates and displays the result in a message like:
	“The area of a circle with a radius of 5.2 is 84.9056”
3. Sale
    A store is having a sale in which a 10% discount is applied to purchases over $20.  Write a script that prompts for a total price and prints the discounted price (if it qualifies).
4. Length Converter 
    Write a script that first prompts for a length in feet and then for a unit to convert to with 4 unit options. Print a message with the converted length based on which option they selected. Also, handle the case where the user doesn’t enter one of the expected options.
    You may use any units you’d like and any messages you’d like but you may use the screenshot below as a guide
"""
import math

class AssignmentTwo:
    #1 Fahrenheit to Celsius
    fahrenheit = float(input("Please input the temperature in degrees Fahrenheit.\n"))
    print(str(fahrenheit) + " degrees Fahrenheit is " + str(round((fahrenheit - 32)*(5/9), 2)) + " degrees Celsius.\n")
    
    #2 Area of a Circle
    radius = float(input("Please input the radius of a given circle.\n"))
    print("The area of a circle with radius, " + str(radius) + ", is " + str(round(math.pi * (radius**2), 2)) + ".\n")
   
    #3 Sale
    total = float(input("Please input the total.\n$"))
    print("Your total is $" + str(round(total, 2)) + ".\n" if total<=20 else "Your total is $" + str(round(total*.9, 2)) + ".\n")
    
    #4 Length Converter
    feet = float(input("Please enter a length in feet.\n"))
    unit = input("Please enter one of the given units:\nYards, Inches, Centimeters, Meters\n")
    if(unit.lower() == "yards"):
        print(str(feet) + " feet is equal to " + str(round(feet/3, 2)) + " yards.")
    elif(unit.lower() == "inches"):
        print(str(feet) + " feet is equal to " + str(feet*12) + " inches.")
    elif(unit.lower() == "centimeters"):
        print(str(feet) + " feet is equal to " + str(round(feet*30.48, 2)) + " centimeters.")
    elif(unit.lower() == "meters"):
        print(str(feet) + " feet is equal to " + str(round(feet*.3048, 3)) + " meters.")
    else:
        print("Unexpected unit input.\nPlease try again.")
        
    input("Press enter to close.")