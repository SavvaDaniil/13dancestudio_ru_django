
from dataclasses import dataclass


@dataclass
class StyleLiteViewModel:
    id: int
    name: str
    link_short: str
    posterSrc: str
    is_bigger: bool
    is_lower: bool