from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px

from typing import List

import src.components.ids as ids
from data.schema import DataSchema as schema
from src.language import __t__
from data.DataSource import DataSource


def plot_pokemon_stats(source: DataSource, idx: int, type_list: List[str]):
    norm_stats = source.get_stat_normalized_columns(idx, type_list)
    title = source.generate_title(idx, __t__)

    fig = px.bar(x=schema.STAT_COLS, y=source.get_all_stats(idx),
                 color=norm_stats, color_continuous_scale="earth",
                 range_color=(-2, 2), title=title)

    fig.update_layout(xaxis_title=__t__('general', "stats"),
                      yaxis_title=__t__('general', "base_stats"),
                      coloraxis_colorbar_title_text=__t__('general', "relative"))
    return fig


def create_stat_bar_chart(source: DataSource, idx: int, type_list: List[str]):
    fig = plot_pokemon_stats(source, idx, type_list)
    image_url = source.get_pokemon_image(idx)

    return dbc.Row([
        html.Div(dcc.Graph(figure=fig), className="col"),
        html.Div(
            html.Img(src=image_url, alt=" " + __t__('general', "no_image"), width="80%"),
            className="col"
        )
    ])


def render(app: Dash, source: DataSource) -> html.Div:

    @app.callback(
        Output(ids.STAT_BAR_CHART, "children"),
        [Input(ids.POKEMON_DROPDOWN, "value"), Input(ids.TYPE_DROPDOWN, "value")]
    )
    def _update_stat_pokemon(selected_pokemon: List[int], type_list: List[str]) -> List[dcc.Graph]:
        if selected_pokemon is None:
            return []

        return [create_stat_bar_chart(source, i, type_list) for i in selected_pokemon]

    return html.Div(id=ids.STAT_BAR_CHART)


if __name__ == '__main__':
    source = DataSource("data/ExampleData.csv")
    fig = plot_pokemon_stats(source, 0, ["Grass"])
    fig.show()
