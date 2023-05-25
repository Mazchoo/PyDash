from dash import Dash, html, dcc
import pandas as pd

import src.components.ids as ids
from data.schema import DataSchema as schema


def render(app: Dash, type_df: pd.DataFrame) -> html.Div:
    all_types = type_df[schema.TYPE].unique()

    return html.Div(
        className="container",
        children=[
            html.H6("Type benchmark"),
            dcc.Dropdown(
                id=ids.TYPE_DROPDOWN,
                options=[{"label": k, "value": k} for k in all_types],
                multi=True,
                value=all_types,
                placeholder="Benchmark will be the average of all pokemon (which is not the same as all types)"
            )
        ]
    )
