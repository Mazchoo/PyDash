from dash import Dash, html

import src.components.pokemon_dropdown as pokemon_dropdown
import src.components.stats_bar_chart as stats_bar_chart


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div container",
        children=[
            html.Br(),
            html.H1(app.title),
            html.Hr(),
            html.P("Hello There"),
            pokemon_dropdown.render(app),
            html.Hr(),
            stats_bar_chart.render(app)
        ]
    )
