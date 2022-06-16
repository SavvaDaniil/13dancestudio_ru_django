from dataclasses import dataclass, asdict
import json
from typing import List

from dancestudio13_ru.ViewModel.Teacher.TeacherInfoViewModel import TeacherInfoViewModel
from dancestudio13_ru.ViewModel.Teacher.TeacherLiteViewModel import TeacherLiteViewModel
from dancestudio13_ru.ViewModel.DanceGroup.DanceGroupLiteViewModel import DanceGroupLiteViewModel

@dataclass
class JsonAnswerStatus:
    status: str
    errors: str

    teacherInfoViewModel: TeacherInfoViewModel = None
    teacherLiteViewModels: List[TeacherLiteViewModel] = None
    danceGroupLiteViewModels: List[DanceGroupLiteViewModel] = None

    @property
    def __dict__(self):
        """
        get a python dictionary
        """
        return asdict(self)
        
    @property
    def json(self):
        """
        get the json formated string
        """
        return json.dumps(self.__dict__)