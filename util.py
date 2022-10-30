import operator
from collections import OrderedDict

import matplotlib.pyplot as plt
import numpy as np


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


def plot_event_probabilities(event_probabilities: dict):
    fig, ax = plt.subplots(clear=True)

    sorted_probas = OrderedDict(sorted(event_probabilities.items(), key=operator.itemgetter(1), reverse=True))

    x_values = list(sorted_probas.keys())
    y_values = list(sorted_probas.values())
    ax.bar(x_values, y_values)
    ax.set_xticks(x_values)
