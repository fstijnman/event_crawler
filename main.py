import re
import requests
import json
import datetime
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")


def get_paradiso_events():
    """
    Get paradiso data from API
    """
    logging.debug("Getting paradiso events")
    paradiso_events_api = "https://api.paradiso.nl/api/events?lang=nl&start_time=now&sort=date&order=asc&limit=1000&page=1&with=locations"

    resp = requests.get(url=paradiso_events_api)
    events_data = resp.json()
    event_data = []
    for event in events_data:
        paradiso_event_api = (
            f"https://api.paradiso.nl/api/library/lists/events/{event['id']}?lang=nl"
        )
        resp_event = requests.get(url=paradiso_event_api)
        event_data.append(resp_event.json()[0])

    return events_data, event_data


def test_paradiso(retrieval_date):
    """
    Test function dumps events and event data paradiso
    """
    paradiso_events_data, paradiso_event_data = get_paradiso_events()
    with open(
        f'data/{retrieval_date.strftime("%Y%m%d")}_paradiso_events_data.json', "w"
    ) as outfile:
        json.dump(paradiso_events_data, outfile)

    with open(
        f'data/{retrieval_date.strftime("%Y%m%d")}_paradiso_event_data.json', "w"
    ) as outfile:
        json.dump(paradiso_event_data, outfile)


def get_melkweg_events():
    """
    Get melkweg data from page source
    """
    logging.debug("Getting melkweg events")

    melkweg_event_url = (
        "https://www.melkweg.nl/nl/agenda/as_json/1/grouped/0/page_size/-1"
    )

    resp = requests.get(url=melkweg_event_url)
    events_data = resp.json()

    return events_data


def test_melkweg(retrieval_date):
    """
    Test function dumps events and event data paradiso
    """
    melkweg_events_data = get_melkweg_events()
    with open(
        f'data/{retrieval_date.strftime("%Y%m%d")}_melkweg_events_data.json', "w"
    ) as outfile:
        json.dump(melkweg_events_data, outfile)


def main():
    today = datetime.date.today()

    test_paradiso(today)
    test_melkweg(today)


if __name__ == "__main__":
    main()
