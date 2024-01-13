#Python program, converting degress into Fahrenheit, Celsius, and Kelvin units

#Welcome user to the program
print("Welcome to TEMPERATURE CONVERTER")

#Loop program until a 0 or quit is entered 
while True: 
    #Prompt user for input:
    unit = input("Please specify which unit you'd like to enter: (1 - Fahrenheit 'F', 2 - Celsius 'C', or 3 - Kelvin 'K') \n(To exit this program type '0' or 'Quit') ").lower()

    #If exit input is declared
    if unit == "0" or unit == "quit":
        print("You have now exited this program...")
        break

    #Determine user input outcome
    #If Fahrenheit was chosen:
    if unit == "fahrenheit" or unit == "f" or unit == "1":
        print("You chose: Fahrenheit")
        #Prompt user for temperature #
        tempF = input("Enter the temperature you'd like to enter: ")
        print(tempF + " Fahrenheit to Celsius & Kelvin")
        #Convert input into float
        f = float(tempF)
        #Convert to celsius
        c = (f - 32) * 5/9
        #Convert to kelvin
        k = (f - 32) * 5/9 + 273.15
        #Print Results
        print(str(c) + " Celsius")
        print(str(k) + " Kelvin")
    #Else if Celsius was chosen
    elif unit == "celsius" or unit == "c" or unit == "2":
        print("You chose: Celsius")
        #Prompt user for temperature #
        tempC = input("Enter the temperature you'd like to enter: ")
        print(tempC + " Celsius to Fahrenheit & Kelvin")
        #Convert input into float
        c = float(tempC)
        #Convert to fahrenheit
        f = (c * 9/5) + 32
        #Convert to kelvin
        k = c + 273.15
        #Print results
        print(str(f) + " Fahrenheit")
        print(str(k) + " Kelvin")
    #Else if Kelvin was chosen
    elif unit == "kelvin" or unit == "k" or unit == "3":
        print("You chose: Kelvin")
        #Prompt user for temperature #
        tempK = input("Enter the temperature you'd like to enter: ")
        print(tempK + " Kelvin to Fahrenheit & Celsius")
        #Convert input into float
        k = float(tempK)
        #Convert to fahrenheit
        f = (k - 273.15) * 9/5 + 32
        #Convert to celsius
        c = k - 273.15
        #Print results
        print(str(f) + " Fahrenheit")
        print(str(c) + " Celsius")
    #Otherwise incorrect input was entered and needs to be run agin:
    else:
        print("INCORRECT INPUT! You entered: " + unit)
