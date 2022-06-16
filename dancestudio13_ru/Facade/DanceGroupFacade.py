#from turtle import pos
from dancestudio13_ru.Repository.DanceGroupRepository import DanceGroupRepository
from dancestudio13_ru.ViewModel.DanceGroup.DanceGroupLiteViewModel import DanceGroupLiteViewModel
from dancestudio13_ru.Facade.StyleFacade import StyleFacade
from dancestudio13_ru.Facade.TeacherFacade import TeacherFacade
from typing import List
import dataclasses

class DanceGroupFacade:

    def listAllLiteActive(self) -> List[DanceGroupLiteViewModel]:
        danceGroupRepository = DanceGroupRepository()
        danceGroups = danceGroupRepository.listAllActive()
        danceGroupLiteViewModel: List[DanceGroupLiteViewModel] = []

        styleFacade = StyleFacade()
        teacherFacade = TeacherFacade()

        for danceGroup in danceGroups:
            danceGroupLiteViewModel.append(
                dataclasses.asdict(DanceGroupLiteViewModel(
                    id=danceGroup.id,
                    name = danceGroup.name,
                    level=danceGroup.level,
                    isSpecialCourse=danceGroup.isSpecialCourse,
                    active= danceGroup.active,
                    ...

                    styleLiteViewModel=(styleFacade.getLiteViewModel(style = danceGroup.style) if danceGroup.style else None),
                    teacherLiteViewModel=(teacherFacade.getLiteViewModel(teacher = danceGroup.teacher) if danceGroup.teacher else None)

                )
                )
            )

        return danceGroupLiteViewModel