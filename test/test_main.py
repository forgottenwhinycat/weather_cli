import pytest
from app.main import get_weather

def test_get_weather_valid(monkeypatch):
    class MockResponse:
        def __init__(self):
            self.status_code = 200
        def json(self):
            return {
                "name": "Kyiv",
                "main": {"temp": 22},
                "weather": [{"description": "clear sky"}]
            }

    monkeypatch.setattr("requests.get", lambda url: MockResponse())
    result = get_weather("Kyiv")
    assert result["city"] == "Kyiv"
    assert result["temperature"] == 22

def test_get_weather_invalid(monkeypatch):
    class MockResponse:
        def __init__(self):
            self.status_code = 404
        def json(self):
            return {"message": "city not found"}

    monkeypatch.setattr("requests.get", lambda url: MockResponse())
    with pytest.raises(ValueError):
        get_weather("FakeCity")
