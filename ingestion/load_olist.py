import logging
from pathlib import Path

from sqlalchemy import create_engine

from config import load_settings
from csv_reader import CsvReader
from datasets import DATASETS
from postgres_loader import PostgresLoader


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logger = logging.getLogger(__name__)


def run(project_root: Path) -> None:
    settings = load_settings(project_root)
    engine = create_engine(settings.database_url)

    try:
        with engine.connect():
            logger.info("Database connection successful")

        reader = CsvReader()
        loader = PostgresLoader(
            engine=engine,
            schema=settings.schema,
            chunksize=settings.chunksize,
        )

        for dataset in DATASETS:
            dataframe = reader.read(settings.data_dir / dataset.filename)
            logger.info(
                "Read %s records from %s",
                len(dataframe),
                dataset.filename,
            )
            loader.load(dataframe, dataset.table_name)

        logger.info("All datasets loaded successfully")

    finally:
        engine.dispose()


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]
    run(project_root)