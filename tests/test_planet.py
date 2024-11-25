from src.model.planet import Planet


def test_planet():
    planet = Planet("name", 3, 3, 3)
    assert planet.upgraded_stats.earn == 20
    assert planet.upgraded_stats.delay == 5
