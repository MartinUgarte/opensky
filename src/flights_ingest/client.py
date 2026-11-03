import requests


def parse_bbox(raw):
    lamin, lomin, lamax, lomax = (float(x) for x in raw.split(","))
    return {"lamin": lamin, "lomin": lomin, "lamax": lamax, "lomax": lomax}


def fetch_states(base_url, bbox):
    resp = requests.get(f"{base_url}/states/all", params=bbox, timeout=10)
    resp.raise_for_status()
    return resp.json()["states"]
