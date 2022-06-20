from lab3 import exp_val_est, weighted_var_est, var_est
import numpy as np


if __name__ == '__main__':
    n = [10, 100, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]

    for n_of_samples in n:
        samples = np.random.standard_cauchy(n_of_samples)

        est_ex = exp_val_est(samples)
        est_wvar = weighted_var_est(samples)
        est_var = var_est(samples)

        print(f'Estimates for n = {n_of_samples}\n'
              f'Expected Value Est. = {est_ex}\n'
              f'Weighted Variance Est. = {est_wvar}\n'
              f'Variance Est. = {est_var}\n')

