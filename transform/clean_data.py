import pandas as pd

def parse_standings(data):
    """Transforme le classement brut en DataFrame propre"""
    standings = data["standings"][0]["table"]
    rows = []
    for entry in standings:
        rows.append({
            "position":        entry["position"],
            "team":            entry["team"]["name"],
            "played":          entry["playedGames"],
            "won":             entry["won"],
            "draw":            entry["draw"],
            "lost":            entry["lost"],
            "goals_for":       entry["goalsFor"],
            "goals_against":   entry["goalsAgainst"],
            "goal_diff":       entry["goalDifference"],
            "points":          entry["points"],
        })
    df = pd.DataFrame(rows)
    df["win_rate"] = (df["won"] / df["played"]).round(2)
    df["goals_per_game"] = (df["goals_for"] / df["played"]).round(2)
    return df

def parse_matches(data):
    """Transforme les matchs bruts en DataFrame propre"""
    matches = data["matches"]
    rows = []
    for m in matches:
        rows.append({
            "date":          m["utcDate"][:10],
            "matchday":      m["matchday"],
            "home_team":     m["homeTeam"]["name"],
            "away_team":     m["awayTeam"]["name"],
            "home_score":    m["score"]["fullTime"]["home"],
            "away_score":    m["score"]["fullTime"]["away"],
            "status":        m["status"],
            "winner":        m["score"]["winner"],
        })
    df = pd.DataFrame(rows)
    # Garder uniquement les matchs terminés
    df = df[df["status"] == "FINISHED"].copy()
    df["date"] = pd.to_datetime(df["date"])
    df["total_goals"] = df["home_score"] + df["away_score"]
    return df

def parse_scorers(data):
    """Transforme les buteurs bruts en DataFrame propre"""
    scorers = data["scorers"]
    rows = []
    for s in scorers:
        rows.append({
            "player":    s["player"]["name"],
            "team":      s["team"]["name"],
            "goals":     int(s["goals"]) if s["goals"] else 0,
            "assists":   int(s["assists"]) if s.get("assists") else 0,
            "penalties": int(s["penalties"]) if s.get("penalties") else 0,
        })
    df = pd.DataFrame(rows)
    return df

if __name__ == "__main__":
    from extract.fetch_data import get_standings, get_matches, get_top_scorers

    print("Test transformation...")
    df_standings = parse_standings(get_standings("FL1"))
    df_matches   = parse_matches(get_matches("FL1"))
    df_scorers   = parse_scorers(get_top_scorers("FL1"))

    print(f"✅ Classement : {len(df_standings)} équipes")
    print(df_standings[["position","team","points","win_rate"]].head())
    print(f"\n✅ Matchs terminés : {len(df_matches)}")
    print(f"✅ Buteurs : {len(df_scorers)}")