import i18n

LOCALE = "en"
i18n.load_path.append("locale")
i18n.set("locale", LOCALE)


def __t__(category: str, word: str):
    return i18n.t(f"{category}.{word}")
