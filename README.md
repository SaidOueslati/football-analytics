# ⚽ Football Analytics Pipeline

> Pipeline ETL complet + modèle de Machine Learning pour analyser et prédire les résultats de la Ligue 1 2025/2026.

## 🏗️ Architecture
API Football-Data.org

↓

Extract (requests)

↓

Transform (Pandas)

↓

Load (PostgreSQL)

↓

Analyse (matplotlib/seaborn)

↓

ML (scikit-learn / Random Forest)

## 📊 Visualisations

| Classement Ligue 1 | Buts par journée | Top Buteurs |
|---|---|---|
| ![classement](analysis/classement.png) | ![buts](analysis/buts_par_journee.png) | ![buteurs](analysis/top_buteurs.png) |

## 🤖 Modèle ML — Prédiction de résultats

- **Algorithme :** Random Forest Classifier (scikit-learn)
- **Features :** win_rate, goals_per_game, points (domicile & extérieur)
- **Accuracy : 48%** — cohérent avec la littérature sur la prédiction de matchs de football
- **Dataset :** 305 matchs terminés, saison 2025/2026

![feature importance](ml/feature_importance.png)

## 🛠️ Stack technique

| Couche | Technologie |
|---|---|
| Extraction | Python · requests · API REST |
| Transformation | Pandas |
| Stockage | PostgreSQL · psycopg2 |
| Analyse | matplotlib · seaborn |
| Machine Learning | scikit-learn (Random Forest) |
| Conteneurisation | Docker · Docker Compose |
| Environnement | python-dotenv · Git |

## 🚀 Lancer le projet

### ⚡ Option 1 — Docker (recommandé)

La façon la plus simple de lancer le projet entier en une seule commande :

```bash
# 1. Cloner le repo
git clone https://github.com/SaidOueslati/football-analytics.git
cd football-analytics

# 2. Configurer les variables d'environnement
cp .env.example .env
# Remplir API_KEY dans .env

# 3. Lancer PostgreSQL + pipeline ETL automatiquement
docker-compose up
```

Docker lance automatiquement :
- 🐘 Un container **PostgreSQL** avec le schéma initialisé
- 🐍 Un container **Python** qui installe les dépendances et exécute le pipeline

### 🔧 Option 2 — Installation locale

```bash
# 1. Cloner le repo
git clone https://github.com/SaidOueslati/football-analytics.git
cd football-analytics

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Configurer les variables d'environnement
cp .env.example .env
# Remplir API_KEY et credentials PostgreSQL

# 4. Lancer le pipeline ETL
python main.py

# 5. Lancer le modèle ML
python -m ml.predict
```


## 📁 Structure du projet
football-analytics/

├── extract/        # Appels API football-data.org

├── transform/      # Nettoyage et enrichissement Pandas

├── load/           # Chargement PostgreSQL

├── analysis/       # Visualisations matplotlib/seaborn

├── ml/             # Modèle Random Forest

├── sql/            # Schéma de la base de données

├── docker-compose.yml

├── requirements.txt

└── main.py         # Point d'entrée du pipeline ETL

## 👤 Auteur

**Said Oueslati** — L3 Informatique, Université Paris Cité  
[LinkedIn](https://www.linkedin.com/in/said-oueslati-9432a2208/) · [GitHub](https://github.com/SaidOueslati)