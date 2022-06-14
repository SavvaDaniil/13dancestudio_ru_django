
from dataclasses import dataclass


@dataclass
class TeacherLiteViewModel:
    id: int
    name: str
    schedule_as_str: str
    link_short: str
    posterSrc: str
