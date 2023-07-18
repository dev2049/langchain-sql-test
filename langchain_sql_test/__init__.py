"""langchain_sql_test package."""
from importlib import metadata

from langchain_sql_test.main import MyChain

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""

__all__ = [__version__, "MyChain"]
