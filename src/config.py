import toml
from pprint import pp


def _load_config(config_file="./data/config.toml"):
    with open(config_file, "r") as file:
        config = toml.load(file)
    return config


config = _load_config()

if config.get("debug"):
    print("Debug mode enabled.")
    pp(config)
