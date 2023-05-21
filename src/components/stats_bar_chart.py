from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from typing import List

import src.components.ids as ids
STAT_COLS = ["hp", "attack", "defense", "sp_attack", "sp_defense", "speed"]

df = pd.read_csv("data/ExampleData.csv", index_col=0)
for col in STAT_COLS:
    df[col + '_norm'] = (df[col] - df[col].mean()) / df[col].std()


def plot_pokemon_stats(idx: int):
    df_row = df.iloc[idx]
    fig = px.bar(x=STAT_COLS, y=df.iloc[idx][STAT_COLS],
                 color=[df_row[f"{c}_norm"] for c in STAT_COLS],
                 color_continuous_scale="earth",
                 title=f"<b>Statistics for {df_row['name']} #{df_row['pokedex_number']}")
    fig.update_layout(xaxis_title="Stats", yaxis_title="Base Stat",
                      coloraxis_colorbar_title_text="Relative")
    return fig


def create_bar_chart_for_pokemon(idx: int):
    fig = plot_pokemon_stats(idx)
    return dcc.Graph(figure=fig)


def render(app: Dash) -> html.Div:

    @app.callback(
        Output(ids.STAT_BAR_CHART, "children"),
        Input(ids.POKEMON_DROPDOWN, "value")
    )
    def _update_stat_pokemon(selected_pokemon: List[str]) -> List[dcc.Graph]:
        if selected_pokemon is None:
            return []
        return [create_bar_chart_for_pokemon(i) for i in selected_pokemon]

    return html.Div(id=ids.STAT_BAR_CHART)


if __name__ == '__main__':
    fig = plot_pokemon_stats(0)
    fig.show()
