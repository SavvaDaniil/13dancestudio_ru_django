
from dataclasses import dataclass
from dancestudio13_ru.ViewModel.Style.StyleLiteViewModel import StyleLiteViewModel
from dancestudio13_ru.ViewModel.Teacher.TeacherLiteViewModel import TeacherLiteViewModel

@dataclass
class DanceGroupLiteViewModel:
    
    id: int
    name: str
    level: int
    isSpecialCourse: bool
    active: bool
    ...

    styleLiteViewModel: StyleLiteViewModel
    teacherLiteViewModel: TeacherLiteViewModel