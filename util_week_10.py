import numpy as np


def get_errors(n: int) -> np.ndarray:
    true_lambda = 5
    return np.random.poisson(true_lambda, size=n)

def get_measurements(n: int) -> np.ndarray:
    true_mu = 5.0
    true_sigma = 2.0
    return np.random.normal(true_mu, true_sigma, size=n)