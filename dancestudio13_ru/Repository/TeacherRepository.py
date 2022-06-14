
from numpy import dtype
from dancestudio13_ru.models import Teacher
from typing import List

class TeacherRepository:

    def findById(self, id_of_teacher: int) -> Teacher:
        teacher = Teacher.objects.get(id = id_of_teacher)
        return teacher

    def findByLinkShort(self, link_short: str) -> Teacher:
        teacher = Teacher.objects.get(link_short = link_short)
        return teacher

    def listAllActive(self, offset: int = 0, limit: int = 18) -> List[Teacher]:
        teachers = Teacher.objects.filter(active=1).order_by("-order_number")[offset:limit]
        return teachers

    def listAll(self) -> List[Teacher]:
        teachers = Teacher.objects.all()
        teachers.reverse()
        return teachers