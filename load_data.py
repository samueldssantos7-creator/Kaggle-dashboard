from pathlib import Path
import pandas as pd
import sys
import argparse

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR  # ajuste para PROJECT_DIR / "data" se preferir

def find_csvs(data_dir: Path):
    return [p for p in data_dir.iterdir() if p.is_file() and p.suffix.lower() == ".csv"]

def load_csv(path: Path, nrows=None, chunksize=None, dtype=None):
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    if chunksize:
        chunks = []
        for chunk in pd.read_csv(path, chunksize=chunksize, dtype=dtype):
            chunks.append(chunk)
        return pd.concat(chunks, ignore_index=True)
    return pd.read_csv(path, nrows=nrows, dtype=dtype)

def choose_target(csvs, choice=None):
    if choice:
        p = Path(choice)
        # caminho absoluto/relativo válido
        if p.exists() and p.is_file():
            return p.resolve()
        choice_lower = choice.lower()
        # procurar por nome exato ou sem extensão (stem)
        matches = [c for c in csvs if c.name.lower() == choice_lower or c.stem.lower() == choice_lower]
        if matches:
            return matches[0]
        raise FileNotFoundError(f"Arquivo não encontrado: {choice}")
    # default: primeiro CSV válido na pasta
    if csvs:
        return csvs[0]
    raise FileNotFoundError("Nenhum arquivo .csv válido encontrado.")

def run(target_path: Path):
    print("\nCarregando:", target_path)
    df = load_csv(target_path, nrows=None, chunksize=None)
    print("Dimensões:", df.shape)
    print("Colunas:", list(df.columns[:20]))
    print("\nResumo rápido (head):")
    print(df.head().to_string(index=False))

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    out_clean = PROJECT_DIR / f"clean_{target_path.name}"
    df.to_csv(out_clean, index=False)
    print("\nArquivo limpo salvo em:", out_clean)

def main(argv=None):
    parser = argparse.ArgumentParser(description="Carrega CSV(s) do projeto Kaggle")
    parser.add_argument("file", nargs="?", help="Global_Climate_Change_Data_2020_2025.csv")
    args = parser.parse_args(argv)

    csvs = find_csvs(DATA_DIR)
    if not csvs and not args.file:
        print("Nenhum arquivo CSV encontrado em:", DATA_DIR)
        sys.exit(1)

    if csvs:
        print("Arquivos CSV encontrados:")
        for i, f in enumerate(csvs, 1):
            print(f"{i}. {f.name}  ({f.stat().st_size//1024} KB)")

    try:
        target = choose_target(csvs, args.file)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    run(target)

if __name__ == "__main__":
    main()