import toml


def _load_data(data_file: str):
    with open(data_file, "r") as file:
        data = toml.load(file)
    return data


config = _load_data("data/config.toml")
data = _load_data("data/game.toml")
settings = _load_data("data/settings.toml")
