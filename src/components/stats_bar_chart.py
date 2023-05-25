from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from typing import List
import requests

import src.components.ids as ids
import src.components.fallback_image as fallback_image
from data.schema import DataSchema as schema


def get_stat_normalized_columns(df_row: pd.Series, bench_df: pd.DataFrame) -> List[float]:
    return [(df_row[s] - bench_df[s]["mean"]) / bench_df[s]["std"] for s in schema.STAT_COLS]


def generate_title(df_row: pd.Series) -> str:
    title = f"<b>{df_row[schema.NAME]} #{df_row[schema.POKEDEX_NO]}"
    title += f" [{df_row[schema.TYPE1]}"
    if not pd.isnull(df_row[schema.TYPE2]):
        title += f" / {df_row[schema.TYPE2]}"
    title += f"] <br>{df_row[schema.JAPAN_NAME]}"
    return title


def plot_pokemon_stats(idx: int, df: pd.DataFrame, benchmark_df: pd.DataFrame):
    df_row = df.iloc[idx]
    norm_stats = get_stat_normalized_columns(df_row, benchmark_df)
    title = generate_title(df_row)

    fig = px.bar(x=schema.STAT_COLS, y=df_row[schema.STAT_COLS],
                 color=norm_stats, color_continuous_scale="earth",
                 range_color=(-2, 2), title=title)

    fig.update_layout(xaxis_title="Stats", yaxis_title="Base Stat",
                      coloraxis_colorbar_title_text="Relative")
    return fig


def get_pokemon_image(pokemon_name: str):
    image_url = f"https://img.pokemondb.net/artwork/large/{pokemon_name}.jpg"

    if requests.get(image_url).status_code != 200:
        image_url = fallback_image.IMAGE_FALLBACK

    return image_url


def create_bar_chart_for_pokemon(idx: int, df: pd.DataFrame, benchmark_df: pd.DataFrame):
    fig = plot_pokemon_stats(idx, df, benchmark_df)
    image_url = get_pokemon_image(df.iloc[idx][schema.NAME].lower())

    return dbc.Row([
        html.Div(dcc.Graph(figure=fig), className="col"),
        html.Div(
            html.Img(src=image_url, alt=" No Image", width="80%"),
            className="col"
        )
    ])


def render(app: Dash, df: pd.DataFrame, type_df: pd.DataFrame) -> html.Div:

    @app.callback(
        Output(ids.STAT_BAR_CHART, "children"),
        [Input(ids.POKEMON_DROPDOWN, "value"), Input(ids.TYPE_DROPDOWN, "value")]
    )
    def _update_stat_pokemon(selected_pokemon: List[int], type_list: List[str]) -> List[dcc.Graph]:
        if selected_pokemon is None:
            return []

        sel_type_df = type_df.loc[type_df[schema.TYPE].isin(type_list)]
        if sel_type_df.empty:
            sel_type_df = df

        bench_df = pd.DataFrame.from_dict({
            s: {"mean": sel_type_df[s].mean(), "std": sel_type_df[s].mean()}
            for s in schema.STAT_COLS
        })

        return [create_bar_chart_for_pokemon(i, df, bench_df) for i in selected_pokemon]

    return html.Div(id=ids.STAT_BAR_CHART)


if __name__ == '__main__':
    fig = plot_pokemon_stats(0)
    fig.show()
