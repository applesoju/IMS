import sys
import random
import numpy as np
import matplotlib.pyplot as plt


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def plot_generator(z):
    x = np.linspace(0, 1, 1000)
    y = x * z - np.floor(x * z)

    plt.plot(x, y, linewidth=4)
    plt.title('Generator function')
    plt.xlabel('Xn')
    plt.ylabel('Xn+1')
    plt.show()


def plot_values(random_numbers):
    x = np.linspace(0, len(random_numbers), len(random_numbers))
    colors = np.random.rand(len(random_numbers))
    plt.scatter(x, random_numbers, alpha=0.5, c=colors)
    plt.title('All generated numbers')
    plt.xlabel('Sample number')
    plt.ylabel('Sample value')
    plt.show()


def plot_histogram(random_numbers):
    v_count = [0] * 10

    for n in random_numbers:
        if 0 <= n <= 0.1:
            v_count[0] += 1
        elif 0.1 < n <= 0.2:
            v_count[1] += 1
        elif 0.2 < n <= 0.3:
            v_count[2] += 1
        elif 0.3 < n <= 0.4:
            v_count[3] += 1
        elif 0.4 < n <= 0.5:
            v_count[4] += 1
        elif 0.5 < n <= 0.6:
            v_count[5] += 1
        elif 0.6 < n <= 0.7:
            v_count[6] += 1
        elif 0.7 < n <= 0.8:
            v_count[7] += 1
        elif 0.8 < n <= 0.9:
            v_count[8] += 1
        else:
            v_count[9] += 1

    plt.bar(np.arange(0.05, 1.05, step=0.1), np.array(v_count), width=0.1, edgecolor='black')
    plt.title('np.random.uniform() output')
    plt.xlabel('Sample value')
    plt.ylabel('Amount of samples')
    plt.xticks(np.round(np.arange(0, 1.1, step=0.1), 1), np.round(np.arange(0, 1.1, step=0.1), 1))
    plt.show()


def sawblade_rand(x0, z, n):
    x_next = x0
    output = np.empty(n)
    # cycle_detected = False

    for i in range(0, n):
        # if i % 1000 == 0 and i != 0:
        #     print(i)

        # if not cycle_detected and x_next in output:
        #     print(f'Cycle detected on X{i}')
        #     cycle_detected = True

        output[i] = x_next
        x_next = x_next * z - np.floor(x_next * z)
        # x_next = round(x_next * z - np.floor(x_next * z), 2)

    return output


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Incorrect number of arguments.')
        exit()

    elif not is_number(sys.argv[1]) or not is_number(sys.argv[2])\
            or not sys.argv[3].isnumeric():
        print('Incorrect arguments.')
        exit()

    x_first = float(sys.argv[1])        # First value for pseudorandom number generator
    z_param = float(sys.argv[2])        # Z parameter - number of "sawblades"
    iterations = int(sys.argv[3])       # Number of iterations

    if x_first == 0:
        x_first = random.random()

    if z_param == 0:
        z_param = random.random() * random.randint(1, 999)

    print(f'X0 = {x_first}, z = {z_param}, Iterations = {iterations}.')

    out = sawblade_rand(x_first, z_param, iterations)
    # out = np.random.uniform(0, 1, iterations)

    # Plot a graph which represents the generator
    # plot_generator(z_param)

    # Plot all generated numbers
    # plot_values(out)

    # Plot a histogram of generated numbers
    plot_histogram(out)
