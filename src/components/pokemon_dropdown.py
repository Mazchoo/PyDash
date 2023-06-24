from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import random
import pandas as pd

from typing import List

import src.components.ids as ids
from data.schema import DataSchema as schema
from src.language import __t__, LOCALE


def render(app: Dash, df: pd.DataFrame) -> html.Div:
    all_pokemon = df[schema.GERMAN_NAME if LOCALE == "de" else schema.NAME]
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
            html.H6(__t__("general", "select_pokemon")),
            dcc.Dropdown(
                id=ids.POKEMON_DROPDOWN,
                options=[{"label": k, "value": i} for k, i in zip(all_pokemon, dex_number)],
                multi=True,
                placeholder=__t__("general", "select_something")
            ),
            html.Br(),
            html.Button(
                className="drop-down-button",
                id=ids.SELECT_RANDOM_POKEMON,
                children=[__t__("general", "select_random")]
            )
        ]
    )
