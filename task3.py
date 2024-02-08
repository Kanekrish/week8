import matplotlib.pyplot as plt

def coordinate():
    # Prompt user to enter an x value
    x = float(input("Enter an x value: "))

    # Prompt user to enter a y value
    y = float(input("Enter a y value: "))

    # Return a tuple containing x and y
    return (x, y)

def path():
    # Display the message "Retrieving path..."
    print("Retrieving path...")

    # Create empty lists for x values and y values
    x_values = []
    y_values = []

    # Iterate 4 times and collect coordinates from user
    for i in range(4):
        # Call the coordinate function and store result
        data = coordinate()

        # Add x value to x_values list
        x_values.append(data[0])

        # Add y value to y_values list
        y_values.append(data[1])

    # Return a list containing x values and y values
    return [x_values, y_values]

def run_task3():
    # Retrieve path coordinates using path function
    values = path()

    # Display a line plot with red dashed line and circle markers
    plt.plot(values[0], values[1], color='red', linestyle='dashed', marker='o')

    # Add labels for x and y axes
    plt.xlabel('X Values')
    plt.ylabel('Y Values')

    # Display the plot
    plt.show()

run_task3()