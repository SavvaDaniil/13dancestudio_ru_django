#from turtle import pos
from dancestudio13_ru.Repository.StyleRepository import StyleRepository
from dancestudio13_ru.ViewModel.Style.StyleLiteViewModel import StyleLiteViewModel
from dancestudio13_ru.ViewModel.Style.StyleInfoViewModel import StyleInfoViewModel
from dancestudio13_ru.ViewModel.Teacher.TeacherLiteViewModel import TeacherLiteViewModel
from dancestudio13_ru.models import Style, Teacher
from typing import List

class StyleFacade:


    def getInfoByShortLink(self, link_short: str) -> StyleInfoViewModel:
        styleRepository = StyleRepository()
        style = styleRepository.findByLinkShort(link_short=link_short)
        return self.getInfoViewModel(style)

    def getInfoById(self, id_of_style: int) -> StyleInfoViewModel:
        styleRepository = StyleRepository()
        style = styleRepository.findById(id_of_style = id_of_style)
        return self.getInfoViewModel(style)


    def getInfoViewModel(self, style: Style) -> StyleInfoViewModel:
        if style is None:
            return None
        
        teachers: List[Teacher] = style.teachers.all()
        teacherLiteViewModels: List[TeacherLiteViewModel] = []
        if teachers:
            for teacher in teachers:
                if teacher.active == 0:
                    continue
                teacherLiteViewModels.append(
                    TeacherLiteViewModel(
                        id= teacher.id,
                        name=teacher.name,
                        schedule_as_str=teacher.schedule_as_str,
                        link_short=teacher.link_short,
                        posterSrc=teacher.getPosterSrc()
                    )
                )

        return StyleInfoViewModel(
            id=style.id,
            name=style.name,
            description=style.description,
            link_short=style.link_short,
            posterSrc=style.getPosterSrc(),
            videoSrc=(style.video.videoSrc.url if style.video and style.video.videoSrc else None),
            teacherLiteViewModels = teacherLiteViewModels
        )

    def getLiteViewModel(self, style: Style) -> StyleLiteViewModel:
        return StyleLiteViewModel(
            id=style.id,
            name = style.name,
            link_short= style.link_short,
            posterSrc = style.getPosterSrc(),
            is_bigger = style.is_bigger,
            is_lower = style.is_lower
        )

    def listAllLiteActive(self) -> List[StyleLiteViewModel]:
        styleRepository = StyleRepository()
        styles = styleRepository.listAllActive()
        styleLiteViewModel = []

        for style in styles:
            styleLiteViewModel.append(
                self.getLiteViewModel(style)
            )

        return styleLiteViewModel