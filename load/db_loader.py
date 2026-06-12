import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def init_db():
    """Crée les tables si elles n'existent pas"""
    conn = get_connection()
    cur = conn.cursor()
    with open("sql/schema.sql", "r") as f:
        cur.execute(f.read())
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Tables créées")

def load_standings(df):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE standings RESTART IDENTITY")
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO standings
            (position, team, played, won, draw, lost,
             goals_for, goals_against, goal_diff, points,
             win_rate, goals_per_game)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, tuple(row))
    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ {len(df)} équipes chargées")

def load_matches(df):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE matches RESTART IDENTITY")
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO matches
            (date, matchday, home_team, away_team,
             home_score, away_score, status, winner, total_goals)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, tuple(row))
    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ {len(df)} matchs chargés")

def load_scorers(df):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE scorers RESTART IDENTITY")
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO scorers (player, team, goals, assists, penalties)
            VALUES (%s,%s,%s,%s,%s)
        """, tuple(row))
    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ {len(df)} buteurs chargés")

if __name__ == "__main__":
    init_db()