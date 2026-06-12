from extract.fetch_data import get_standings, get_matches, get_top_scorers
from transform.clean_data import parse_standings, parse_matches, parse_scorers
from load.db_loader import load_standings, load_matches, load_scorers

print("🚀 Lancement du pipeline ETL...")

print("\n📥 Extraction des données...")
raw_standings = get_standings("FL1")
raw_matches   = get_matches("FL1")
raw_scorers   = get_top_scorers("FL1")

print("\n🔄 Transformation...")
df_standings = parse_standings(raw_standings)
df_matches   = parse_matches(raw_matches)
df_scorers   = parse_scorers(raw_scorers)

print("\n💾 Chargement dans PostgreSQL...")
load_standings(df_standings)
load_matches(df_matches)
load_scorers(df_scorers)

print("\n✅ Pipeline ETL terminé avec succès !")