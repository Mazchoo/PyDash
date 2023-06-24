from dash import Dash, html

import src.components.pokemon_dropdown as pokemon_dropdown
import src.components.stats_bar_chart as stats_bar_chart
import src.components.benchmark_dropdown as benchmark_dropdown
import data.loader as loader
from src.language import __t__


def create_layout(app: Dash) -> html.Div:
    df, type_df = loader.load_pokemon_data()
    return html.Div(
        className="app-div container",
        children=[
            html.Br(),
            html.H1(app.title),
            html.Hr(),
            html.P(__t__("general", "hello_there")),
            pokemon_dropdown.render(app, df),
            html.Br(),
            benchmark_dropdown.render(app, type_df),
            html.Hr(),
            stats_bar_chart.render(app, df, type_df)
        ]
    )
