import dataclasses
#from turtle import pos
from typing import List
from dancestudio13_ru.models import Teacher, Video
from dancestudio13_ru.ViewModel.Teacher.TeacherLiteViewModel import TeacherLiteViewModel
from dancestudio13_ru.ViewModel.Teacher.TeacherInfoViewModel import TeacherInfoViewModel
from dancestudio13_ru.ViewModel.Video.VideoLiteViewModel import VideoLiteViewModel

from dancestudio13_ru.Repository.TeacherRepository import TeacherRepository

class TeacherFacade:

    def getInfoByShortLink(self, link_short: str) -> TeacherInfoViewModel:
        teacherRepository = TeacherRepository()
        teacher = teacherRepository.findByLinkShort(link_short=link_short)
        return self.getInfoViewModel(teacher)

    def getInfoById(self, id_of_teacher: int) -> TeacherInfoViewModel:
        teacherRepository = TeacherRepository()
        teacher = teacherRepository.findById(id_of_teacher = id_of_teacher)
        return self.getInfoViewModel(teacher)


    def getInfoViewModel(self, teacher: Teacher) -> TeacherInfoViewModel:
        if teacher is None:
            return None
        
        videos: List[Video] = teacher.videos.all()
        videoLiteViewModels = []
        if videos:
            for video in videos:
                if video.active == 0:
                    continue
                videoLiteViewModels.append(
                    VideoLiteViewModel(
                        id= video.id,
                        videoSrc= (video.videoSrc.url if video.videoSrc is not None else None)
                    )
                )

        return TeacherInfoViewModel(
            id=teacher.id,
            name=teacher.name,
            schedule_as_str = teacher.schedule_as_str,
            description=teacher.description,
            link_short=teacher.link_short,
            posterSrc=teacher.getPosterSrc(),
            videoLiteViewModels = videoLiteViewModels
        )

    def getLiteViewModel(self, teacher: Teacher) -> TeacherLiteViewModel:
        return TeacherLiteViewModel(
            id=teacher.id,
            name=teacher.name,
            schedule_as_str=teacher.schedule_as_str,
            link_short=(teacher.link_short if teacher.link_short is not None else str(teacher.id)),
            posterSrc=teacher.getPosterSrc()
        )

    def search(self, offset: int, limit: int) -> List[TeacherLiteViewModel]:
        teacherRepository = TeacherRepository()
        teachers = teacherRepository.listAllActive(offset, limit)
        teacherLiteViewModels = []

        for teacher in teachers:
            teacherLiteViewModels.append(
                dataclasses.asdict(self.getLiteViewModel(teacher= teacher))
            )

        return teacherLiteViewModels


    def listFirst6LiteActive(self) -> List[TeacherLiteViewModel]:
        return self.search(0, 6)


    def listAllLiteActive(self) -> List[TeacherLiteViewModel]:
        teacherRepository = TeacherRepository()
        teachers = teacherRepository.listAllActive()

        teacherLiteViewModels = []

        for teacher in teachers:
            teacherLiteViewModels.append(
                dataclasses.asdict(self.getLiteViewModel(teacher= teacher))
            )
            
        return teacherLiteViewModels
