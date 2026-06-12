import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import numpy as np 

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def load_data():
    conn = get_connection()
    df_matches = pd.read_sql("SELECT * FROM matches", conn)
    df_standings = pd.read_sql("SELECT * FROM standings", conn)
    conn.close()
    return df_matches, df_standings

def build_features(df_matches, df_standings):
    """enrichit chaque match avec les stats des équipes"""
    stats = df_standings.set_index("team")[["win_rate", "goals_per_game", "points"]]

    df = df_matches[df_matches["winner"].notna()].copy()

    #Ajout des stats de chaque équipe
    df["home_win_rate"] = df["home_team"].map(stats["win_rate"])
    df["away_win_rate"] = df["away_team"].map(stats["win_rate"])
    df["home_goals_per_game"] = df["home_team"].map(stats["goals_per_game"])
    df["away_goals_per_game"] = df["away_team"].map(stats["goals_per_game"])
    df["home_points"] = df["home_team"].map(stats["points"])
    df["away_points"] = df["away_team"].map(stats["points"])

    #features et target
    features = [
        "home_win_rate", "away_win_rate",
        "home_goals_per_game", "away_goals_per_game",
        "home_points", "away_points"
    ]

    df = df.dropna(subset=features + ["winner"])
    X = df[features]
    Y = df["winner"]

    return X , Y

def train_model(X, y):
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"\n✅ Accuracy : {acc:.2%}")
    print("\n📊 Rapport de classification :")
    print(classification_report(y_test, y_pred,
          target_names=le.classes_))

    return model, le, acc

def plot_feature_importance(model, feature_names):
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]

    plt.figure(figsize=(10, 5))
    plt.bar(range(len(feature_names)),
            importances[indices], color="steelblue")
    plt.xticks(range(len(feature_names)),
               [feature_names[i] for i in indices], rotation=45, ha="right")
    plt.title("🔍 Importance des features — Prédiction résultat match",
              fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.savefig("ml/feature_importance.png", dpi=150)
    plt.show()
    print("✅ Graphique sauvegardé")

if __name__ == "__main__":
    print("🚀 Chargement des données...")
    df_matches, df_standings = load_data()

    print("⚙️  Construction des features...")
    X, y = build_features(df_matches, df_standings)
    print(f"   {len(X)} matchs utilisés pour l'entraînement")

    print("\n🤖 Entraînement du modèle Random Forest...")
    model, le, acc = train_model(X, y)

    print("\n📊 Importance des features...")
    plot_feature_importance(model, X.columns.tolist())


