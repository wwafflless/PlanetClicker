from planetclicker.settings import Settings


def test_setting():
    gs = Settings()
    assert gs.Graphics.fps == 30.0
