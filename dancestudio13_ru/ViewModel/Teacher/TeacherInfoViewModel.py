from dataclasses import dataclass
from typing import List
from dancestudio13_ru.ViewModel.Video.VideoLiteViewModel import VideoLiteViewModel


@dataclass
class TeacherInfoViewModel:
    id: int
    name: str
    schedule_as_str: str
    description: str
    link_short: str
    posterSrc: str
    videoLiteViewModels: List[VideoLiteViewModel]