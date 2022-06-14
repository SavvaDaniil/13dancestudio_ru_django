from dancestudio13_ru.models import Abonement
from typing import List


class AbonementRepository:

    def listAllActive(self) -> List[Abonement]:
        abonements = Abonement.objects.filter(active=1).order_by("-order_number")
        return abonements