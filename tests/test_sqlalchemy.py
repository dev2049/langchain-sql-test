import langchain  # noqa: F401
import sqlalchemy


def test_configure_mappers() -> None:
    sqlalchemy.orm.configure_mappers()
