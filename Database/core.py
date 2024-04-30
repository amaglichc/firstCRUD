from typing import Annotated

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, mapped_column, declarative_base

engine = create_engine(
    url="postgresql+psycopg://postgres:postgres@localhost:5432/python_test",
    echo=True
)
session_maker = sessionmaker(engine)

intpk = Annotated[int, mapped_column(primary_key=True)]


Base = declarative_base()


def create_tables() -> None:
    with engine.begin() as conn:
        Base.metadata.drop_all(conn)
        Base.metadata.create_all(conn)
