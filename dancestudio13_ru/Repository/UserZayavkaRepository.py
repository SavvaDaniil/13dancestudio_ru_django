import datetime
from dancestudio13_ru.models import UserZayavka

class UserZayavkaRepository:

    def add(self, name: str, phone: str, ip_address: str, date_of_add: str) -> UserZayavka:
        ...
        return userZayavka
