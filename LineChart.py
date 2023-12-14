#Importing in order for line graph to be created
import matplotlib as mpl
import matplotlib.pyplot as plt

# Function
def lineChart():
    # Dictionary to store data points (x-values and corresponding y-values)
    data = {}

    # Infinite loop to continuously get user input until "done" is entered
    while True:
        # Prompting the user to enter one ordered pair separated by a comma
        pair = input("Please enter ONE ordered pair, no parentheses, separated by a comma (ex: \"0, 2\"): ")

        # Checking if the user entered "done" to exit the loop
        if pair == "done":
            break

        # Checking if the entered pair contains exactly one comma
        if pair.count(",") != 1:
            print("Please make sure it is 1 ordered pair")
            continue

        # Splitting the entered pair into x and y values
        pair = pair.split(",")
        pair[0] = pair[0].strip()  # Stripping leading and trailing whitespaces
        pair[1] = pair[1].strip() 

        # Trying to convert the entered values to integers
        try:
            pair[0] = int(pair[0])
            pair[1] = int(pair[1])
        except:
            print("Make sure only numbers are being inputted for the ordered pair")
            continue

        # Adding the pair to the data dictionary
        data[pair[0]] = pair[1]

        # Displaying a message indicating that the pair has been added
        print("Pair added.")
        print("If finished, enter \"done\"")

    # Sorting the data points by x-values to ensure the line chart doesn't move backward
    datax = list(data.keys())
    datax.sort()
    sortedData = {}
    for i in datax:
        sortedData[i] = data[i]
    datay = list(sortedData.values())

    # Plotting the line chart with markers for data points
    plt.plot(datax, datay, marker='o')

    # Displaying the plot
    plt.show()
