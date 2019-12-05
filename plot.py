import matplotlib.pyplot as plt

def plot_result(input_dots, a, b):
    x_vector = []
    y_vector = []
    for item in input_dots:
        x_vector.append(item[0])
        y_vector.append(item[1])
    z_vector = [float(-(a/b)*item[0])for item in input_dots]
    plt.plot(x_vector,y_vector, label="input dots", linestyle="dashed")
    plt.plot(x_vector, z_vector, label="PCA reconstructed")
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")
    plt.show()
