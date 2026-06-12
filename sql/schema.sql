-- Création de la base
CREATE TABLE IF NOT EXISTS standings (
    id              SERIAL PRIMARY KEY,
    position        INT,
    team            VARCHAR(100),
    played          INT,
    won             INT,
    draw            INT,
    lost            INT,
    goals_for       INT,
    goals_against   INT,
    goal_diff       INT,
    points          INT,
    win_rate        FLOAT,
    goals_per_game  FLOAT,
    updated_at      TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS matches (
    id              SERIAL PRIMARY KEY,
    date            DATE,
    matchday        INT,
    home_team       VARCHAR(100),
    away_team       VARCHAR(100),
    home_score      INT,
    away_score      INT,
    status          VARCHAR(50),
    winner          VARCHAR(50),
    total_goals     INT,
    updated_at      TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS scorers (
    id          SERIAL PRIMARY KEY,
    player      VARCHAR(100),
    team        VARCHAR(100),
    goals       INT,
    assists     INT,
    penalties   INT,
    updated_at  TIMESTAMP DEFAULT NOW()
);