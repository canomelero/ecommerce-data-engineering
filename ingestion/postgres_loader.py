import logging

import pandas as pd
from sqlalchemy import Engine


logger = logging.getLogger(__name__)


class PostgresLoader:
    def __init__(
        self,
        engine: Engine,
        schema: str,
        chunksize: int,
    ) -> None:
        self.engine = engine
        self.schema = schema
        self.chunksize = chunksize

    def load(self, dataframe: pd.DataFrame, table_name: str) -> None:
        dataframe.to_sql(
            name=table_name,
            con=self.engine,
            schema=self.schema,
            if_exists="replace",
            index=False,
            chunksize=self.chunksize,
        )

        logger.info(
            "Loaded %s records into %s.%s",
            len(dataframe),
            self.schema,
            table_name,
        )