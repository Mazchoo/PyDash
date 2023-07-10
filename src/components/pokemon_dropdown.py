from dash import Dash, html, dcc
from dash.dependencies import Input, Output

from typing import List

from data.DataSource import DataSource
import src.components.ids as ids
from src.language import __t__


def render(app: Dash, source: DataSource) -> html.Div:

    @app.callback(
        Output(ids.POKEMON_DROPDOWN, "value"),
        Input(ids.SELECT_RANDOM_POKEMON, "n_clicks")
    )
    def _select_random_pokemon(n_clicks: int) -> List[str]:
        if n_clicks is not None:
            return source.get_random_poke_id()

    return html.Div(
        className="container",
        children=[
            html.H6(__t__("general", "select_pokemon")),
            dcc.Dropdown(
                id=ids.POKEMON_DROPDOWN,
                options=source.get_all_pokemon_options(),
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
