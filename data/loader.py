import pandas as pd
from typing import Tuple

from data.schema import DataSchema as schema


def get_all_pokemon_of_type(df: pd.DataFrame, find_type: str):
    type_df = df.loc[~pd.isnull(df[find_type])][schema.STAT_COLS + [find_type]]
    return type_df.rename(columns={find_type: schema.TYPE})


def create_type_dataframe(df: pd.DataFrame):
    type_df_1 = get_all_pokemon_of_type(df, schema.TYPE1)
    type_df_2 = get_all_pokemon_of_type(df, schema.TYPE2)
    return pd.concat([type_df_1, type_df_2])


def load_pokemon_data(path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    df = pd.read_csv(path, index_col=0)

    for norm_col, col in zip(schema.STAT_NORM_COLS, schema.STAT_COLS):
        df[norm_col] = (df[col] - df[col].mean()) / df[col].std()
        df[norm_col] = df[norm_col].astype(float)

    type_df = create_type_dataframe(df)

    return df, type_df
