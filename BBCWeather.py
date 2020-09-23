import feedparser
import requests


location_codes = {"Cambridge": "2653941", "Manchester": "2643123"}
#

#rfgergergerg


def fetch_forecast(location: str):
    """ Fetches the 3 day forecast from the BBC Weather api

    Args:
        location (str): The city that you want the forecast for

    Yields:
        dict: The URL (unique ID) of the forecast, the summary description and the date it was published
    """
    f = feedparser.parse(f"https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/{location_codes[location]}")
    for entry in f["entries"]:
        yield {
            "url": entry["id"],
            "summary": entry["summary"],
            "published": entry["published"],
        }


def location_to_code(location: str):
    """ Requests the location code for a given location name

    Args:
        location (str): The city that we want the location code for

    Returns:
        str: The location code for the given city
    """
    params = {
        "api_key": "AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv",
        "stack": "aws",
        "locale": "en",
        "filter": "international",
        "s": location,
        "a": "true",
        "format": "json",
    }
    try:
        r = requests.get("https://locator-service.api.bbci.co.uk/locations", params=params).json()
        return r["response"]["results"]["results"][0]["id"]
    except KeyError:
        pass

