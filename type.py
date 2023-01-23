from typing import (
    List,
    NamedTuple
)


Header = List[str]


class Row(NamedTuple):
    STATE:    str
    STATEFP:  str
    CD113FP:  str
    NAMELSAD: str


class Districts(NamedTuple):
    header: Header
    data:   List[Row]