from dataclasses import dataclass
from typing import List

from dancestudio13_ru.ViewModel.Teacher.TeacherInfoViewModel import TeacherInfoViewModel

@dataclass
class JsonAnswerStatus:
    status: str
    errors: str

    teacherInfoViewModel: TeacherInfoViewModel