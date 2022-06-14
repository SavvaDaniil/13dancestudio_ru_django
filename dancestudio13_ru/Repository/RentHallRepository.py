
from dancestudio13_ru.models import RentHall

class RentHallRepository:

    def listAllActive(self):
        return RentHall.objects.filter(active=1).order_by("-order_number")