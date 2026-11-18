from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    data_dir: Path
    database_url: str
    schema: str = "raw"
    chunksize: int = 5_000


def load_settings(project_root: Path) -> Settings:
    load_dotenv(project_root / ".env")

    required = ("POSTGRES_USER", "POSTGRES_PASSWORD", "POSTGRES_DB")
    missing = [name for name in required if not os.getenv(name)]

    if missing:
        raise RuntimeError(
            f"Missing required environment variables: {', '.join(missing)}"
        )

    user = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5433")
    database = os.environ["POSTGRES_DB"]

    database_url = (
        f"postgresql+psycopg://{user}:{password}@"
        f"{host}:{port}/{database}"
    )

    return Settings(
        data_dir=project_root / "data" / "raw" / "olist",
        database_url=database_url,
    )