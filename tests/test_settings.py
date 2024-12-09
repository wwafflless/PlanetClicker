from planetclicker.settings import settings


def test_setting():
    lang = settings.gets("ui", "lang")
    assert lang == "en-us"
