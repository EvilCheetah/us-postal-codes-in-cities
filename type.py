from pathlib import Path
from typing import (
    List,
    NamedTuple
)


Filename   = Path
Filenames  = List[Filename]

Header     = List[str]


class Row(NamedTuple):
    STATE:    str
    STATEFP:  str
    CD113FP:  str
    NAMELSAD: str


class Districts(NamedTuple):
    header: Header
    data:   List[Row]