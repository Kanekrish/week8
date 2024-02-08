import matplotlib.pyplot as plt

def small():
    # Create a small square with a red dotted line and circle markers
    plt.plot([-1, 1], [-1, 1], color='red', linestyle='dotted', marker='o')
    plt.plot([1, 1], [-1,1], color='red', linestyle='dotted', marker='o')
    plt.plot([-1, -1], [-1, 1], color='red', linestyle='dotted', marker='o')
    plt.plot([-1, -1], [1,1], color='red', linestyle='dotted', marker='o')

def medium():
    # Create a medium square around the small square with a green dashed line and square markers
    plt.plot([-2, 2], [-2, 2], color='green', linestyle='dashed', marker='s')
    plt.plot([2, 2], [-2,2], color='green', linestyle='dashed', marker='s')
    plt.plot([-2, -2], [-2, 2], color='green', linestyle='dashed', marker='s')
    plt.plot([-2, -2], [2,2], color='green', linestyle='dashed', marker='s')

def large():
    # Create a large square around the medium square with a blue solid line and pentagon markers
    plt.plot([-3, 3], [-3, 3], color='blue', linestyle='solid', marker='p')
    plt.plot([3, 3], [-3,3], color='blue', linestyle='solid', marker='p')
    plt.plot([-3, -3], [-3, 3], color='blue', linestyle='solid', marker='p')
    plt.plot([-3, -3], [3,3], color='blue', linestyle='solid', marker='p')

small()
medium()
large()

plt.show()