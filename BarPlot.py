# Importing matplotlib for creating a bar plot
import matplotlib as mpl
import matplotlib.pyplot as plt

# Function 
def barPlot():
    # Dictionary to store data for the bar plot (bar names and values)
    data = {}

    # Infinite loop to get user input until "done" is entered
    while True:
        # Prompting the user to enter a bar's name and value separated by a comma
        bar = input("Enter the bar's name and value, separated by a comma (ex: \"June, 14\"): ")
        
        # Checking if the user entered "done" to exit the loop
        if bar == "done":
            break
        
        # Checking if the entered bar contains exactly one comma
        if bar.count(",") != 1:
            print("Make sure you only enter 1 bar at a time")
            continue

        # Splitting the entered bar into name and value
        bar = bar.split(",")
        bar[0] = bar[0].strip()  # Stripping leading and trailing whitespaces
        bar[1] = bar[1].strip()

        # Checking if the value part is a digit
        if not bar[1].isdigit():
            print("Make sure that you are entering a NUMBER after the comma for the value of the bar")
            continue

        # Adding the bar to the data dictionary
        data[bar[0]] = int(bar[1])

        # Displaying a message indicating that the data has been successfully added
        print("Data successfully added.")
        print("If you are finished adding bars, enter \"done\".\n")
    
    # Extracting names and values from the dictionary for plotting
    barTitles = list(data.keys())
    barValues = list(data.values())

    # Creating a bar plot using the entered data
    plt.bar(barTitles, barValues)

    # Displaying the plot
    plt.show()
