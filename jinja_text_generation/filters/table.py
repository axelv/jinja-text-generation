from typing import TypedDict, Any
from .pprint import do_pprint

class TableHeader(TypedDict):
    id: str
    name: str

class Table(TypedDict):
    header: list[TableHeader] 
    data: list[dict[str, Any]]

def do_pad_column(content:str, table, column, char:str=" "):
    """Return the width of a column in a table."""
    header = table["header"]
    rows = table["data"]
    col_lengths = [len(do_pprint(row[header[column - 1]["id"]])) for row in rows]
    col_lengths.append(len(header[column - 1]["name"]))
    n_chars =  max(col_lengths)
    return content.ljust(n_chars, char)