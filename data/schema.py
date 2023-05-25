
class DataSchema:
    HP = "hp"
    ATTACK = "attack"
    DEFENSE = "defense"
    SP_ATTACK = "sp_attack"
    SP_DEFENSE = "sp_defense"
    SPEED = "speed"
    STAT_COLS = [HP, ATTACK, DEFENSE, SP_ATTACK, SP_DEFENSE, SPEED]
    STAT_NORM_COLS = [f"{col}_norm" for col in STAT_COLS]
    NAME = "name"
    TYPE1 = "type_1"
    TYPE2 = "type_2"
    TYPE = "type"
    POKEDEX_NO = 'pokedex_number'
    JAPAN_NAME = "japanese_name"
