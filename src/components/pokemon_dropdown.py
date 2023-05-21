from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from typing import List
import random
import pandas as pd

import src.components.ids as ids


def render(app: Dash) -> html.Div:
    df = pd.read_csv("data/ExampleData.csv", index_col=0)
    all_pokemon = df["name"]
    dex_number = df.index

    @app.callback(
        Output(ids.POKEMON_DROPDOWN, "value"),
        Input(ids.SELECT_RANDOM_POKEMON, "n_clicks")
    )
    def _select_random_pokemon(n_clicks: int) -> List[str]:
        if n_clicks is not None:
            return [random.choice(dex_number)]

    return html.Div(
        className="container",
        children=[
            html.H6("Select a Pokemon"),
            dcc.Dropdown(
                id=ids.POKEMON_DROPDOWN,
                options=[{"label": k, "value": i} for k, i in zip(all_pokemon, dex_number)],
                multi=True,
                placeholder="Select something dude"
            ),
            html.Br(),
            html.Button(
                className="drop-down-button",
                id=ids.SELECT_RANDOM_POKEMON,
                children=["Select Random"]
            )
        ]
    )
