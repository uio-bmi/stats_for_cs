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
    import plotly.express as px

    fig = px.bar(x=list(event_probabilities.keys()), y=list(event_probabilities.values()))
    fig.update_layout(yaxis_title='estimated<br>probability', xaxis={'title': 'event'}, template='plotly_white',
                      showlegend=False)
    fig.show()


def plot_probability_comparison(event_probabilities_simulation, event_probabilities_formula):
    import plotly.graph_objects as go

    fig = go.Figure(data=[
        go.Bar(name='formula', x=list(event_probabilities_formula.keys()),
               y=list(event_probabilities_formula.values())),
        go.Bar(name='simulation', x=list(event_probabilities_simulation.keys()),
               y=list(event_probabilities_simulation.values()))])
    fig.update_layout(barmode='group', yaxis_title='(estimated)<br>probability', xaxis={'title': 'event'},
                      template='plotly_white', showlegend=True)

    fig.show()
