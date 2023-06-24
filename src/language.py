import i18n
from data.schema import DataSchema as schema

LOCALE = "en"
i18n.load_path.append("locale")
i18n.set("locale", LOCALE)


def __t__(category: str, word: str):
    return i18n.t(f"{category}.{word}")


def get_schema_name():
    return schema.GERMAN_NAME if LOCALE == 'de' else schema.NAME
