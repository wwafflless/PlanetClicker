from planetclicker.data import planets, config, settings
import json


def test_planets_loader():
    assert len(planets.gets("planet")) == 8


def test_config_loader():
    assert config.gets("game", "difficulty") == "easy"
    assert config.gets("locale", "timezone") == "pst"
    assert config.gets("locale", "language") == "en-us"
    assert config.gets("font", "title", "path") == "ThaleahFat.ttf"
    assert config.gets("font", "title", "size") == 20

    assert "v_1" in config.gets("bind", "panel", "overview")
    assert "v_k" in config.gets("bind", "camera", "up")


def test_settings_loader():
    assert settings.gets("ui", "language") == ["en-us"]

    assert settings.gets("graphics", "resolution") == [
        dict(width=640, height=480),
        dict(width=1280, height=720),
        dict(width=1920, height=1080),
        dict(width=2560, height=1440),
        dict(width=3840, height=2160),
    ]
