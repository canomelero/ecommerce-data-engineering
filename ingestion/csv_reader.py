from pathlib import Path

import pandas as pd


class CsvReader:
    def read(self, path: Path) -> pd.DataFrame:
        if not path.is_file():
            raise FileNotFoundError(f"CSV file not found: {path}")

        return pd.read_csv(
            path,
            dtype=str,
            keep_default_na=False,
        )