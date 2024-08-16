import numpy as np
import pandas as pd


def get_iris_dataset():
    import plotly.express as px
    return px.data.iris()


def plot_many_values_with_mean(values, plot_title: str = ""):
    import plotly.graph_objects as go

    mean = np.mean(values)
    values.sort()
    vals_for_plotting = np.unique(values, return_counts=True)
    y1_mean = max(vals_for_plotting[1])

    fig = go.Figure(data=[go.Bar(x=vals_for_plotting[0], y=vals_for_plotting[1], name='results'),
                          go.Scatter(x=[mean, mean], y=[0, y1_mean], mode='lines')])

    fig.add_annotation(x=mean, y=y1_mean, text=f"mean={mean}", showarrow=False, yshift=10)

    fig.update_layout(yaxis_title='counts', xaxis={'title': 'result'}, template='plotly_white',
                      showlegend=False, title=plot_title)
    fig.show()
