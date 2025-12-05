import random

import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


def coin2():
    return random.sample(['head', 'head', 'tail'], 1)[0]

def coin1():
    return random.sample(['head', 'tail'], 1)[0]


def plot_binomial_distribution_example():
    import plotly.graph_objects as go
    from scipy.stats import binom

    # Parameters
    n = 3  # number of trials
    p = 0.5  # fair coin

    # Possible outcomes
    x = [0, 1, 2, 3]

    # Compute probabilities using SciPy's binomial PMF
    probs = binom.pmf(x, n, p)

    # Create bar plot
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=x,
        y=probs,
        width=0.5
    ))

    # Layout formatting
    fig.update_layout(
        title="Probability of Getting 0–3 Heads in 3 Fair Coin Tosses",
        xaxis_title="Number of Heads",
        yaxis_title="Probability",
        yaxis=dict(range=[0, max(probs) * 1.2]),
        template='plotly_white',
        width=600,
        height=400
    )

    fig.show()


def plot_bernoulli_examples():
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    from scipy.stats import bernoulli

    # Define outcomes
    x = [0, 1]

    # Bernoulli probabilities to plot
    p_values = [0.2, 0.5, 0.8]

    # Create subplots: 1 row, 3 columns
    fig = make_subplots(rows=1, cols=3, subplot_titles=[f"p = {p}" for p in p_values])

    for i, p in enumerate(p_values, start=1):
        probs = bernoulli.pmf(x, p)
        fig.add_trace(
            go.Bar(x=x, y=probs, width=0.4),
            row=1, col=i
        )
        # Customize x-axis labels for each subplot
        fig.update_xaxes(
            tickmode='array', tickvals=x, ticktext=['0 (Failure)', '1 (Success)'], row=1, col=i
        )
        fig.update_yaxes(range=[0, 1], row=1, col=i)  # same y-axis scale for comparison

    # Update overall layout
    fig.update_layout(
        title_text="Bernoulli Distribution for Different p Values",
        showlegend=False,
        width=900,  # total figure width
        height=400,
        template='plotly_white'
    )

    fig.show()

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

    fig = go.Figure(go.Bar(
        x=x,
        y=probs,
        width=0.6
    ))

    fig.update_layout(
        title="Uniform Distribution – Roll of a Fair Die",
        xaxis_title="Outcome",
        yaxis_title="Probability",
        yaxis=dict(range=[0, max(probs)*1.2]),
        width=600,
        height=400,
        template='plotly_white'
    )

    fig.show()


def plot_event_probabilities(event_probabilities: dict):
    fig = px.bar(x=list(event_probabilities.keys()), y=list(event_probabilities.values()))
    fig.update_layout(yaxis_title='estimated<br>probability', xaxis={'title': 'event'}, template='plotly_white',
                      showlegend=False, width=600, height=400)
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
