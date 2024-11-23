import toml


def _load_data(data_file="data/game.toml"):
    with open(data_file, "r") as file:
        data = toml.load(file)
    return data


data = _load_data()
