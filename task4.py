import random
import matplotlib.pyplot as plt


def data():
    """
    Function to collect user input for line style, color, and marker style.
    Returns a dictionary containing the user's choices.
    """
    # Create an empty dictionary named paths
    paths = {}

    # Ask the user for line style
    line_style = input("Enter the type of line you would like (:, --, or -): ")

    # Ask the user for color
    color = input("Enter the color you would like (r, g, or b): ")

    # Ask the user for marker style
    marker_style = input("Enter the style of marker you would like (o, s, or ^): ")

    # Store the user's choices in the dictionary
    paths['line_style'] = line_style
    paths['color'] = color
    paths['marker_style'] = marker_style

    # Return the dictionary
    return paths


def generate():
    """
    Function to generate and display a line graph based on user input.
    """
    # Ask the user for the number of lines
    num_lines = int(input("How many lines would you like to display? "))

    for _ in range(num_lines):
        # Call the data function to get user choices
        values = data()

        # Generate random x and y values
        x_values = random.sample(range(1, 11), 5)
        y_values = random.sample(range(1, 11), 5)

        # Display a line graph using user choices and random values
        plt.plot(x_values, y_values, label=f"Line {len(plt.gca().lines) + 1}", linestyle=values['line_style'],
                 color=values['color'], marker=values['marker_style'])

    # Show the legend and plot
    plt.legend()
    plt.title('Line Graph')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()


def run():
    """
    Function to run the program by calling the generate function.
    """
    print("Running....")

    # Call the generate function
    generate()

    print("Done!")


# Example usage:
run()
