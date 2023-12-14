# Importing matplotlib  for creating a scatter plot
import matplotlib as mpl
import matplotlib.pyplot as plt

# Function
def scatterChart():
    # Creating empty lists to store user-inputted data points
    datax = []  # List for x-values
    datay = []  # List for y-values
    
    # Infinite loop initiated
    while True:
        # Prompt user to enter pairs
        pair = input("Please enter ONE ordered pair, no parentheses, separated by a comma (ex: \"0, 2\"): ")
        
        # If 'done' is inputted, break out of loop.
        if pair == "done":
            break
        
        # Making sure only one pair is added
        if pair.count(",") != 1:
            print("Please make sure it is 1 ordered pair")
            continue
        
        # Splitting up inputs
        pair = pair.split(",")
        pair[0] = pair[0].strip()  # Stripping leading and trailing whitespaces
        pair[1] = pair[1].strip()  
        
        # Converting inputs into integers
        try:
            pair[0] = int(pair[0])
            pair[1] = int(pair[1])
        except:
            print("Make sure only numbers are being inputted for the ordered pair")
            continue
        
        # Add the pairs for each value into respective axis
        datax.append(pair[0])
        datay.append(pair[1])
        
        # Confirming pair is added
        print("Pair added.")
        print("If finished, enter \"done\"")

    # Creating a scatter plot using the entered data
    plt.scatter(datax, datay)
    # Displaying the plot
    plt.show()
