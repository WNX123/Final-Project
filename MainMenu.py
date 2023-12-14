# Main menu function with input validation
from BarPlot import barPlot
from BoxPlot import boxPlot
from Pie import pieChart
from ScatterChart import scatterChart
from LineChart import lineChart

import matplotlib as mpl
import matplotlib.pyplot as plt

def MainMenu():
    invalid_input = False
    while True:
        if not invalid_input:
            print("Welcome to our graph creation system!")
            print("Please select what graph you would like to be generated")
            print("1. Bar Plot")
            print("2. Box Plot")
            print("3. Scatter Chart.")
            print("4. Line Chart")
            print("5. Pie")

        # Have User Input Selection
        UserInput = input("Please enter your selection here: ")

        #Validate user input if input is a number 1 - 5 and is not a character. Outputs if it detects that something other than a number 1-5 is produced.
        if UserInput.isdigit():
            UserNum = int(UserInput)

            if 1 <= UserNum <= 5:
                # Valid input, proceed with the corresponding action
                if UserNum == 1:
                    barPlot()
                elif UserNum == 2:
                    boxPlot()
                elif UserNum == 3:
                    scatterChart()
                elif UserNum == 4:
                    lineChart()
                elif UserNum == 5:
                    pieChart()
                 # Ask the user if they want to continue or shut down
                response = input("Do you want to create another graph? (yes/no): ").lower()
                if response != "yes":
                    print("Exiting the program. Goodbye!")
                    return  # Exit the function
                else:
                    invalid_input = False  # Reset the invalid_input flag
            else:
                # Number is outside the specified range of (1,6)
                print("Please enter a number between 1 and 5.")
        else:
            # Input Detected is not a valid number, output that the user needs to input a number 1 - 5.
            print("Only Numbers! Please enter a valid number between 1 and 5.")
            invalid_input = True

#MainMenu Call
MainMenu()

