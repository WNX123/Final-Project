# Importing matplotlib for creating a pie chart
import matplotlib as mpl
import matplotlib.pyplot as plt

# Function 
def pieChart():
    # Dictionary to store data 
    data = {}
    
    # Infinite loop to get user input
    while True:
        # Prompting the user to enter slice's name and value separated by a comma
        pair = input("Enter the slice's name and value, separated by a comma (ex: \"Dogs, 14\"): ")

        # Break if input is 'done'
        if pair == "done":
            break
        
        # Checking if the entered pair contains exactly one comma
        if pair.count(",") != 1:
            print("Make sure you only enter 1 pair at a time")
            continue
        
        # Splitting the entered pair into name and value
        pair = pair.split(",")
        pair[0] = pair[0].strip()  # Stripping leading and trailing whitespaces
        pair[1] = pair[1].strip()  
        
        # Checking if the value part is a digit
        if not pair[1].isdigit():
            print("Make sure that you are entering a NUMBER after the comma for the value of the slice")
            continue
        
        # Adding the pair to the  dictionary
        data[pair[0]] = int(pair[1])
        
        # Displaying a message confirming data is added
        print("Data successfully added.")
        print("If you are finished adding pairs, enter \"done\".\n")
    
    # Extracting names and values from the dictionary for plotting
    sliceNames = list(data.keys())
    sliceValues = list(data.values())

    # Creating a pie chart using the entered data
    plt.pie(sliceValues, labels=sliceNames, autopct='%1.1f%%')

    # Displaying the plot
    plt.show()
