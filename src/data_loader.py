import os
from pathlib import Path
import pandas as pd
import streamlit as st

# caminho local padrão (repo root /data/climate.csv)
DEFAULT_LOCAL = Path(__file__).resolve().parents[1] / "data" / "climate.csv"
# fallback público raw do GitHub (substitua se necessário)
GITHUB_RAW = "https://raw.githubusercontent.com/samueldssantos7-creator/Kaggle-dashboard/main/data/climate.csv"

@st.cache_data
def load_data(path: str | Path | None = None) -> pd.DataFrame:
    """
    Carrega CSV local se existir, senão tenta o raw do GitHub.
    Retorna DataFrame vazio em caso de falha (app trata ausência).
    """
    path = Path(path) if path else DEFAULT_LOCAL

    # tenta local
    if path.exists():
        try:
            df = pd.read_csv(path)
            return df.drop_duplicates()
        except Exception as e:
            st.error(f"Erro ao ler o arquivo local {path}: {e}")
            return pd.DataFrame()

    # tenta raw no GitHub
    try:
        df = pd.read_csv(GITHUB_RAW)
        return df.drop_duplicates()
    except Exception as e:
        st.error(f"Não foi possível carregar dados local nem do GitHub. Erro: {e}")
        return pd.DataFrame()
