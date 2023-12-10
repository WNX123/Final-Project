# Main menu function with input validation
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
            print("5. Histogram")

        # Have User Input Selection
        UserInput = input("Please enter your selection here: ")

        # Validate user input if input is a number 1 - 5 and is not a character. Outputs if it detects that something other than a number 1-5 is produced.
        # if UserInput.isdigit():
        #     UserNum = int(UserInput)

        #     if 1 <= UserNum <= 5:
        #         # Valid input, proceed with the corresponding action
        #         if UserNum == 1:
        #             BarPlot()
        #         elif UserNum == 2:
        #             BoxPlot()
        #         elif UserNum == 3:
        #             ScatterChart()
        #         elif UserNum == 4:
        #             LineChart()
        #         elif UserNum == 5:
        #             Histogram()
        #         break  # Exit the loop after a valid selection
        #     else:
        #         # Number is outside the specified range of (1,6)
        #         print("Please enter a number between 1 and 5.")
        # else:
        #     # Input Detected is not a valid number, output that the user needs to input a number 1 - 5.
        #     print("Only Numbers! Please enter a valid number between 1 and 5.")
        #     invalid_input = True

# MainMenu Call
MainMenu()
