# Import the matplotlib library for plotting
import matplotlib.pyplot as plt

# Define the function `display_line` to create a line plot
def display_line(x_values, y_values):
    # Create a line plot using the given x and y values
    plt.plot(x_values, y_values)

    # Display the plot
    plt.show()

# Define the function `run_task1` to generate and display the line plot
def run_task1():
    # Create lists of x and y values for the plot
    x_values = [1, 2, 3, 4, 5]  # Values for the x-axis
    y_values = [1, 4, 9, 16, 25]  # Corresponding values for the y-axis

    # Call the `display_line` function to create and display the plot
    display_line(x_values, y_values)

# Invoke the `run_task1` function to generate and display the line plot
run_task1()