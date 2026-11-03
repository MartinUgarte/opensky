import requests, json, time

r = requests.get("https://opensky-network.org/api/states/all"
    "?lamin=-35&lomin=-59&lamax=-34&lomax=-58")
data = r.json()
vuelos = []
for s in data["states"]:
    if s[2] == "Argentina":
        vuelos.append({"icao": s[0], "callsign": s[1].strip()})
print("vuelos:", len(vuelos))
f = open("/home/martin/vuelos_" + str(time.time()) + ".json", "w")
json.dump(vuelos, f)
