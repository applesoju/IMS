import sys
import random
import numpy as np
import matplotlib.pyplot as plt


def exp_val_est(x_vec):
    return np.sum(x_vec) / len(x_vec)


def weighted_var_est(x_vec):
    average = exp_val_est(x_vec)
    return np.sum(np.square(x_vec - average)) / len(x_vec)


def var_est(x_vec):
    average = exp_val_est(x_vec)
    return np.sum(np.square(x_vec - average)) / (len(x_vec) - 1)


def generate_sets(avg, std_dev, num_of_sets, n):
    set_list = []
    for i in range(num_of_sets):
        random_set = np.random.normal(avg, std_dev, n)
        set_list.append(random_set)
    return set_list


def empirical_error(avg, std_dev, num_of_sets, n, mode):
    observations = generate_sets(avg, std_dev, num_of_sets, n)
    est_values = np.empty(num_of_sets)
    error = 0

    if mode == 1:
        for i in range(num_of_sets):
            est_values[i] = exp_val_est(observations[i])
        error = np.sum(np.square(est_values - avg)) / num_of_sets

    elif mode == 2:
        for i in range(num_of_sets):
            est_values[i] = weighted_var_est(observations[i])
        error = np.sum(np.square(est_values - std_dev ** 2)) / num_of_sets

    elif mode == 3:
        for i in range(num_of_sets):
            est_values[i] = var_est(observations[i])
        error = np.sum(np.square(est_values - std_dev ** 2)) / num_of_sets

    else:
        print(f'Invalid mode: {mode}\n'
              'Possible modes:'
              '1 - Error of expected value estimation'
              '2 - Error of weighted variance estimation'
              '3 - Error of variance estimation')

    return error


if __name__ == '__main__':
    # rng = np.random.normal(AVG, STD_DEV, N)
    # expected_val = exp_val_est(rng)
    # weighted_var = weighted_var_est(rng)
    # var = var_est(rng)
    #
    # print(f'Est. Avg           = {expected_val}\n'
    #       f'Est. Weighted Var  = {weighted_var}\n'
    #       f'Est. Var           = {var}')

    try:
        mode = int(sys.argv[1])
    except ValueError:
        print(f'Invalid mode: {sys.argv[1]}\n'
              'Possible modes:\n'
              '1 - Error of expected value estimation\n'
              '2 - Error of weighted variance estimation\n'
              '3 - Error of variance estimation\n')
        exit()
    except IndexError:
        print(f'Provide an argument for the mode.\n'
              'Possible modes:\n'
              '1 - Error of expected value estimation\n'
              '2 - Error of weighted variance estimation\n'
              '3 - Error of variance estimation\n')
        exit()

    AVG = 0
    STD_DEV = 4
    L = np.array([10, 100])
    N = np.linspace(100, 10000, 100)
    title_string = ''

    for l_param in L:
        errors = []
        for n_param in N:
            err = empirical_error(AVG, STD_DEV, int(l_param), int(n_param), mode)
            errors.append(err)

        plt.plot(N, errors, linewidth='3')

        if mode == 1:
            title_string = f'Empirical error of Expected Value estimation for L = {l_param}'
        elif mode == 2:
            title_string = f'Empirical error of Weighted Variance estimation for L = {l_param}'
        elif mode == 3:
            title_string = f'Empirical error of Variance estimation for L = {l_param}'
        else:
            print(f'Invalid mode: {mode}\n'
                  'Possible modes:'
                  '1 - Error of expected value estimation'
                  '2 - Error of weighted variance estimation'
                  '3 - Error of variance estimation')
            exit()

        plt.title(title_string)
        plt.ylabel('Error')
        plt.xlabel('Sample number')
        plt.grid()
        plt.show()
