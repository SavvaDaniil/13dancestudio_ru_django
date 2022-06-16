from dancestudio13_ru.Repository.UserZayavkaRepository import UserZayavkaRepository
from dancestudio13_ru.Observer.UserZayavkaObserver import UserZayavkaObserver
import datetime

class UserZayavkaFacade:


    def create(self, name: str, phone: str, ip_address: str) -> bool:
        ...
        return True
