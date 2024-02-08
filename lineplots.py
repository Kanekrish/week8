import matplotlib.pyplot as plt

def coordinate():
    x = input("Please give the value of x:")
    y = input("Please give the value of y:")
    return(x,y)

def path():
    print("Retrieving path...")
    x_value = []
    y_value = []

    for each_time in range(4):
        data = coordinate() # data variable is a tuple
        x_value.append(data[0])
        y_value.append(data[1])
    return[x_values,y_values]

def run_task3():
    values = path()
    plt.plot(values[0],values[1])

run_task3()
plt.show()
