import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def plot_result(input_dots, a, b, fitness_array):
    x_vector = []
    y_vector = []
    for item in input_dots:
        x_vector.append(item[0])
        y_vector.append(item[1])
    z_vector = [float(-(a/b)*item[0]) for item in input_dots]

    # plt.margins(x=0,y=-.25)
    plt.subplot(2,1,1)
    plt.scatter(x_vector,y_vector, label="input dots",color="red")
    plt.plot(x_vector, z_vector, label="PCA reconstructed")
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")
    plt.savefig("result.png")
    fitness_array_x_axis = [i for i in range(len(fitness_array))]
    plt.subplot(2,1,2)
    plt.plot(fitness_array_x_axis, fitness_array, label="growth rate")
    plt.xlabel("time")
    plt.ylabel("fitness")
    plt.show()

