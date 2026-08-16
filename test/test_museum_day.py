# this is the "test/test_museum_day.py" file...

# todo: test the functionality in the "app/museum_day.py" file

from app.museum_day import get_museum_recommendation


def test_rainy_day_recommends_museum():
    # test that a rainy day with moderate temperatures recommends going to the museum
    recommendation = get_museum_recommendation(70, 60, 60)
    assert recommendation["should_go"] == True
    assert recommendation["search_words"] == ["rain", "storm", "umbrella", "clouds"]


def test_hot_day_recommends_museum():
    # test that a hot day recommends going to the museum
    recommendation = get_museum_recommendation(95, 85, 10)
    assert recommendation["should_go"] == True
    assert recommendation["search_words"] == ["sun", "summer", "beach", "garden"]


def test_cold_day_recommends_museum():
    # test that a cold day recommends going to the museum
    recommendation = get_museum_recommendation(30, 20, 10)
    assert recommendation["should_go"] == True
    assert recommendation["search_words"] == ["winter", "snow", "fire", "moon"]


def test_nice_day_does_not_require_museum():
    # test that a nice day does not go to the museum
    recommendation = get_museum_recommendation(75, 65, 10)
    assert recommendation["should_go"] == False
    assert recommendation["search_words"] == ["garden", "flower", "landscape", "bird"]


def test_rain_beats_temperature():
    # even if it's a nice temp, heavy rain chance should still win
    recommendation = get_museum_recommendation(75, 65, 80)
    assert recommendation["should_go"] == True
    assert recommendation["search_words"] == ["rain", "storm", "umbrella", "clouds"]
