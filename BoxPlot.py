# Importing matplotlib for creating a box plot
import matplotlib as mpl
import matplotlib.pyplot as plt

# Function to create a box plot
def boxPlot():
    # List to store data sets for the box plot
    data = []

    # Infinite loop to get user input until "done" is entered
    while True:
        # Prompting the user to enter a comma-separated list of numbers for a data set
        box = input("With only 1 data set at a time, please enter a comma-separated list of numbers to plot: ")

        # Checking if the user entered "done" to exit the loop
        if box == "done":
            break

        # Splitting the entered list into individual values
        box = box.split(",")

        # Trying to convert the entered values to integers
        for i in range(len(box)):
            try:
                box[i] = int(box[i].strip())
            except ValueError:
                print("Please ensure it is a list of numbers.")
                continue

        # Confirmation that dataset has been added
        print("Dataset added.")
        print("If finished, enter \"done\"")
        
        # Adding the dataset to the list of data
        data.append(box)

    # Creating a box plot using the entered data sets
    plt.boxplot(data)
    # Displaying the plot
    plt.show()
