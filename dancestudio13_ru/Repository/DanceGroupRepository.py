from dancestudio13_ru.models import DanceGroup
from typing import List


class DanceGroupRepository:

    def findById(self, id: int) -> DanceGroup:
        danceGroup = DanceGroup.objects.get(id = id)
        return danceGroup

    def listAllActive(self) -> List[DanceGroup]:
        danceGroups = DanceGroup.objects.filter(active=1).order_by("-id")
        return danceGroups