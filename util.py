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


def plot_many_values_with_mean(samples, title=""):
    """Plot probability distribution with mean indicated"""
    fig, ax = plt.subplots(figsize=(6, 4))

    ax.hist(samples, bins=30, density=False, alpha=0.7, color='blue', edgecolor='black')

    mean_value = np.mean(samples)
    ax.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_value:.2f}')
    ax.legend()

    ax.set_title(title)
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')

    plt.tight_layout()
    plt.show()


# === Norske funksjoner / Norwegian functions ===

def mynt1():
    return random.sample(['kron', 'mynt'], 1)[0]

def mynt2():
    return random.sample(['kron', 'kron', 'kron', 'kron', 'mynt'], 1)[0]

def plott_binomialfordeling_eksempel():
    from scipy.stats import binom

    # Parametere
    n = 3  # antall forsøk
    p = 0.5  # rettferdig mynt

    # Mulige utfall
    x = [0, 1, 2, 3]

    # Beregn sannsynligheter med SciPys binomiale PMF
    sannsynligheter = binom.pmf(x, n, p)

    # Lag stolpediagram
    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(x, sannsynligheter, width=0.5)

    ax.set_title("Sannsynlighet for å få 0–3 kron i 3 rettferdige myntkast")
    ax.set_xlabel("Antall kron")
    ax.set_ylabel("Sannsynlighet")
    ax.set_ylim(0, max(sannsynligheter) * 1.2)
    ax.set_xticks(x)

    plt.tight_layout()
    plt.show()

def plott_bernoulli_eksempler():
    from scipy.stats import bernoulli

    # Definer utfall
    x = [0, 1]

    # Bernoulli-sannsynligheter å plotte
    p_verdier = [0.2, 0.5, 0.8]

    # Lag subplots: 1 rad, 3 kolonner
    fig, axes = plt.subplots(1, 3, figsize=(9, 4))
    fig.suptitle("Bernoulli-fordeling for forskjellige p-verdier")

    for i, p in enumerate(p_verdier):
        sannsynligheter = bernoulli.pmf(x, p)
        axes[i].bar(x, sannsynligheter, width=0.4)
        axes[i].set_title(f"p = {p}")
        axes[i].set_xticks(x)
        axes[i].set_xticklabels(['0 (Fiasko)', '1 (Suksess)'])
        axes[i].set_ylim(0, 1)
        axes[i].set_ylabel("Sannsynlighet" if i == 0 else "")

    plt.tight_layout()
    plt.show()

def tell_utfall(utfall_liste):
    """Teller forekomster av hvert utfall i en liste"""
    utfall_oppsummering = {}
    for utfall in utfall_liste:
        if utfall in utfall_oppsummering:
            utfall_oppsummering[utfall] += 1
        else:
            utfall_oppsummering[utfall] = 1
    return utfall_oppsummering

def plott_utfall(utfall_liste, normaliser: bool = False):
    """Plotter utfall som stolpediagram"""
    utfall_oppsummering = tell_utfall(utfall_liste)
    fig, ax = plt.subplots(clear=True)
    x_verdier = list(utfall_oppsummering.keys())

    if normaliser:
        antall_kast = sum(list(utfall_oppsummering.values()))
        y_verdier = np.array(list(utfall_oppsummering.values())) / antall_kast
    else:
        y_verdier = list(utfall_oppsummering.values())

    ax.bar(x_verdier, y_verdier)
    ax.set_xticks(x_verdier)

def plott_uniform_terning():
    """Plotter uniform fordeling for en rettferdig terning"""
    # Mulige utfall
    x = np.arange(1, 7)

    # Uniform sannsynlighet for hver side
    sannsynligheter = np.full(6, 1/6)

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(x, sannsynligheter, width=0.6)

    ax.set_title("Uniform fordeling – Kast av en rettferdig terning")
    ax.set_xlabel("Utfall")
    ax.set_ylabel("Sannsynlighet")
    ax.set_ylim(0, max(sannsynligheter) * 1.2)
    ax.set_xticks(x)

    plt.tight_layout()
    plt.show()

def plott_hendelse_sannsynligheter(hendelse_sannsynligheter: dict, y_tittel='estimert\nsannsynlighet'):
    """Plotter sannsynligheter for hendelser som stolpediagram"""
    fig, ax = plt.subplots(figsize=(6, 4))

    x_verdier = list(hendelse_sannsynligheter.keys())
    y_verdier = list(hendelse_sannsynligheter.values())

    ax.bar(x_verdier, y_verdier)
    ax.set_ylabel(y_tittel)
    ax.set_xlabel('hendelse')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

def plott_sannsynlighet_sammenligning(hendelse_sannsynligheter_simulering, hendelse_sannsynligheter_formel):
    """Sammenligner simulerte og analytiske sannsynligheter i et stolpediagram"""
    # Hent ut data
    x_formel = list(hendelse_sannsynligheter_formel.keys())
    y_formel = list(hendelse_sannsynligheter_formel.values())

    x_sim = list(hendelse_sannsynligheter_simulering.keys())
    y_sim = list(hendelse_sannsynligheter_simulering.values())

    fig, ax = plt.subplots(figsize=(7, 4))

    x_posisjoner = np.arange(len(x_formel))
    stolpe_bredde = 0.35

    stolper1 = ax.bar(x_posisjoner - stolpe_bredde/2, y_formel, stolpe_bredde, label='formel')
    stolper2 = ax.bar(x_posisjoner + stolpe_bredde/2, y_sim, stolpe_bredde, label='simulering')

    # Legg til tekstetiketter på toppen av stolpene
    for stolpe, verdi in zip(stolper1, y_formel):
        ax.annotate(f'{verdi:.2f}', xy=(stolpe.get_x() + stolpe.get_width()/2, stolpe.get_height()),
                    ha='center', va='bottom', fontsize=9)

    for stolpe, verdi in zip(stolper2, y_sim):
        ax.annotate(f'{verdi:.2f}', xy=(stolpe.get_x() + stolpe.get_width()/2, stolpe.get_height()),
                    ha='center', va='bottom', fontsize=9)

    maks_y = max(max(y_formel), max(y_sim))
    ax.set_ylim(0, maks_y * 1.15)

    ax.set_ylabel('(estimert)\nsannsynlighet')
    ax.set_xlabel('hendelse')
    ax.set_xticks(x_posisjoner)
    ax.set_xticklabels(x_formel)
    ax.legend()

    plt.tight_layout()
    plt.show()