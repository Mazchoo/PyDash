from dash import Dash, html, dcc
import pandas as pd

import src.components.ids as ids
from data.schema import DataSchema as schema
from src.language import __t__


def render(app: Dash, type_df: pd.DataFrame) -> html.Div:
    all_types = type_df[schema.TYPE].unique()

    return html.Div(
        className="container",
        children=[
            html.H6(__t__("general", "type_benchmark")),
            dcc.Dropdown(
                id=ids.TYPE_DROPDOWN,
                options=[{"label": __t__("type", k), "value": k} for k in all_types],
                multi=True,
                value=all_types,
                placeholder=__t__("general", "benchmark_average_all")
            )
        ]
    )
