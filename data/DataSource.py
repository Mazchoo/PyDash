import random
import pandas as pd
import requests

from data.loader import load_pokemon_data
from src.language import get_schema_name
from data.schema import DataSchema as schema
import src.components.fallback_image as fallback_image

from functools import lru_cache
from typing import List, Tuple, Callable


class DataSource:

    def __init__(self, path: str):
        self.df, self.type_df = load_pokemon_data(path)

    def get_all_pokemon_options(self):
        all_pokemon = self.df[get_schema_name()]
        dex_number = self.df.index
        name_number_zip = zip(all_pokemon, dex_number)
        return [{"label": k, "value": i} for k, i in name_number_zip]

    def get_random_poke_id(self):
        return [random.choice(self.df.index)]

    def get_all_types(self):
        return self.type_df[schema.TYPE].unique()

    @lru_cache(maxsize=1)
    def _get_benchmark_df(self, type_tuple: Tuple[str]):
        sel_type_df = self.type_df.loc[self.type_df[schema.TYPE].isin(type_tuple)]
        if sel_type_df.empty:
            sel_type_df = self.df

        return pd.DataFrame.from_dict({
            s: {"mean": sel_type_df[s].mean(),
                "std": sel_type_df[s].mean()}
            for s in schema.STAT_COLS
        })

    def get_pokemon_image(self, idx: int):
        pokemon_name = self.df.iloc[idx][schema.NAME].lower()
        image_url = f"https://img.pokemondb.net/artwork/large/{pokemon_name}.jpg"

        if requests.get(image_url).status_code != 200:
            image_url = fallback_image.IMAGE_FALLBACK

        return image_url

    def generate_title(self, idx: int, translator: Callable):
        df_row = self.df.iloc[idx]

        title = f"<b>{df_row[get_schema_name()]}"
        title += f" #{df_row[schema.POKEDEX_NO]}"

        title += f" [{translator('type', df_row[schema.TYPE1])}"
        if not pd.isnull(df_row[schema.TYPE2]):
            title += f" / {translator('type', df_row[schema.TYPE2])}"
        title += f"] <br>{df_row[schema.JAPAN_NAME]}"

        return title

    def get_all_stats(self, idx: int):
        return self.df.iloc[idx][schema.STAT_COLS]

    def get_stat_normalized_columns(self, idx: int, type_list: List[str]) -> List[float]:
        df_row = self.df.iloc[idx]
        bench = self._get_benchmark_df(tuple(type_list))
        return [(df_row[s] - bench[s]["mean"]) / bench[s]["std"] for s in schema.STAT_COLS]
