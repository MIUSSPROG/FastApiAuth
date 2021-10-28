import databases
import sqlalchemy


DATABASE_URL = "sqlite:///test.db"
metadata = sqlalchemy.MetaData()
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL)


class MainMeta:
    metadata = metadata
    database = database

