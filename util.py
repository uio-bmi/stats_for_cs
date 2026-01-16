import random

import matplotlib.pyplot as plt
import numpy as np


def coin2():
    return random.sample(['head', 'head', 'head', 'head', 'tail'], 1)[0]

def coin1():
    return random.sample(['head', 'tail'], 1)[0]


def plot_binomial_distribution_example():
    from scipy.stats import binom

    # Parameters
    n = 3  # number of trials
    p = 0.5  # fair coin

    # Possible outcomes
    x = [0, 1, 2, 3]

    # Compute probabilities using SciPy's binomial PMF
    probs = binom.pmf(x, n, p)

    # Create bar plot
    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(x, probs, width=0.5)

    ax.set_title("Probability of Getting 0–3 Heads in 3 Fair Coin Tosses")
    ax.set_xlabel("Number of Heads")
    ax.set_ylabel("Probability")
    ax.set_ylim(0, max(probs) * 1.2)
    ax.set_xticks(x)

    plt.tight_layout()
    plt.show()


def plot_bernoulli_examples():
    from scipy.stats import bernoulli

    # Define outcomes
    x = [0, 1]

    # Bernoulli probabilities to plot
    p_values = [0.2, 0.5, 0.8]

    # Create subplots: 1 row, 3 columns
    fig, axes = plt.subplots(1, 3, figsize=(9, 4))
    fig.suptitle("Bernoulli Distribution for Different p Values")

    for i, p in enumerate(p_values):
        probs = bernoulli.pmf(x, p)
        axes[i].bar(x, probs, width=0.4)
        axes[i].set_title(f"p = {p}")
        axes[i].set_xticks(x)
        axes[i].set_xticklabels(['0 (Failure)', '1 (Success)'])
        axes[i].set_ylim(0, 1)
        axes[i].set_ylabel("Probability" if i == 0 else "")

    plt.tight_layout()
    plt.show()


def count_outcomes(outcomes):
    outcome_summary = {}
    for outcome in outcomes:
        if outcome in outcome_summary:
            outcome_summary[outcome] += 1
        else:
            outcome_summary[outcome] = 1
    return outcome_summary


def plot_outcomes(outcomes, normalize: bool = False):
    outcomes_summary = count_outcomes(outcomes)
    fig, ax = plt.subplots(clear=True)
    x_values = list(outcomes_summary.keys())

    if normalize:
        toss_count = sum(list(outcomes_summary.values()))
        y_values = np.array(list(outcomes_summary.values())) / toss_count
    else:
        y_values = list(outcomes_summary.values())

    ax.bar(x_values, y_values)
    ax.set_xticks(x_values)


def plot_uniform_die():
    # Possible outcomes
    x = np.arange(1, 7)

    # Uniform probability for each side
    probs = np.full(6, 1/6)

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(x, probs, width=0.6)

    ax.set_title("Uniform Distribution – Roll of a Fair Die")
    ax.set_xlabel("Outcome")
    ax.set_ylabel("Probability")
    ax.set_ylim(0, max(probs) * 1.2)
    ax.set_xticks(x)

    plt.tight_layout()
    plt.show()


def plot_event_probabilities(event_probabilities: dict, y_title='estimated\nprobability'):
    fig, ax = plt.subplots(figsize=(6, 4))

    x_values = list(event_probabilities.keys())
    y_values = list(event_probabilities.values())

    ax.bar(x_values, y_values)
    ax.set_ylabel(y_title)
    ax.set_xlabel('event')

    plt.tight_layout()
    plt.show()


def plot_probability_comparison(event_probabilities_simulation, event_probabilities_formula):
    # Extract data
    x_formula = list(event_probabilities_formula.keys())
    y_formula = list(event_probabilities_formula.values())

    x_sim = list(event_probabilities_simulation.keys())
    y_sim = list(event_probabilities_simulation.values())

    fig, ax = plt.subplots(figsize=(7, 4))

    x_positions = np.arange(len(x_formula))
    bar_width = 0.35

    bars1 = ax.bar(x_positions - bar_width/2, y_formula, bar_width, label='formula')
    bars2 = ax.bar(x_positions + bar_width/2, y_sim, bar_width, label='simulation')

    # Add text labels on top of bars
    for bar, val in zip(bars1, y_formula):
        ax.annotate(f'{val:.2f}', xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                    ha='center', va='bottom', fontsize=9)

    for bar, val in zip(bars2, y_sim):
        ax.annotate(f'{val:.2f}', xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                    ha='center', va='bottom', fontsize=9)

    max_y = max(max(y_formula), max(y_sim))
    ax.set_ylim(0, max_y * 1.15)

    ax.set_ylabel('(estimated)\nprobability')
    ax.set_xlabel('event')
    ax.set_xticks(x_positions)
    ax.set_xticklabels(x_formula)
    ax.legend()

    plt.tight_layout()
    plt.show()