import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.football-data.org/v4"

HEADERS = {"X-Auth-Token": API_KEY}

def get_standings(competition_code="FL1"):
    """Récupère le classement d'une compétition (FL1 = Ligue 1)"""
    url = f"{BASE_URL}/competitions/{competition_code}/standings"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_matches(competition_code="FL1", matchday=None):
    """Récupère les matchs d'une compétition"""
    url = f"{BASE_URL}/competitions/{competition_code}/matches"
    params = {}
    if matchday:
        params["matchday"] = matchday
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_top_scorers(competition_code="FL1"):
    """Récupère les meilleurs buteurs"""
    url = f"{BASE_URL}/competitions/{competition_code}/scorers"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    print("Test de connexion API...")
    data = get_standings("FL1")
    print(f"✅ Connexion OK — Compétition : {data['competition']['name']}")
    print(f"✅ Saison : {data['season']['startDate']} → {data['season']['endDate']}")