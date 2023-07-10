from dash import Dash, html, dcc

import src.components.ids as ids
from src.language import __t__
from data.DataSource import DataSource


def render(app: Dash, source: DataSource) -> html.Div:
    all_types = source.get_all_types()

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
