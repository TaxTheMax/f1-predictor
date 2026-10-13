import requests 
from fastapi import FastAPI, HTTPException

app = FastAPI(title="F1 Predictor API")

@app.get("/api/races/{year}/{round_number}/results")
def get_race_results(year: int, round_number: int):
    url = (f"https://api.jolpi.ca/ergast/f1/"
           f"{year}/{round_number}/results.json")
    try:
        response = requests.get(url, headers={"User-Agent": "F1 Predictor/0.1"}, params={"limit": 100}, timeout=15)
        response.raise_for_status()
        races = response.json()["MRData"]["RaceTable"]["Races"]

    except (requests.RequestException, ValueError, KeyError) as e:
        raise HTTPException(
            status_code=502,
            detail="Unable to retrieve F1 results"
        ) from e

    if not races:
        raise HTTPException(
            status_code=404,
            detail="Race results not found"
        )

    race = races[0]

    return {
        "race": race["raceName"],
        "results": [
            {
                "position": int(result["position"]),
                "driver": (result["Driver"]["givenName"] + " " + result["Driver"]["familyName"]),
                "constructor": result["Constructor"]["name"],
                "points": float(result["points"]),
            }
            for result in race["Results"]
        ]
    }