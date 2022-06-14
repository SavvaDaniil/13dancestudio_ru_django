
from dataclasses import dataclass
from typing import List
from dancestudio13_ru.ViewModel.Teacher.TeacherLiteViewModel import TeacherLiteViewModel


@dataclass
class StyleInfoViewModel:
    id: int
    name: str
    description: str
    link_short: str
    posterSrc: str
    teacherLiteViewModels: List[TeacherLiteViewModel]
