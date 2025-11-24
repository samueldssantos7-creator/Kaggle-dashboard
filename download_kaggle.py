from kaggle.api.kaggle_api_extended import KaggleApi
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent / "data"
OUT_DIR.mkdir(parents=True, exist_ok=True)

api = KaggleApi()
api.authenticate()

# dataset: owner/dataset-name
dataset = "shahzadi786/global-climate-change-data-20202025"

print("Baixando dataset para:", OUT_DIR)
api.dataset_download_files(dataset, path=str(OUT_DIR), unzip=True, quiet=False)

print("Download concluído.")
