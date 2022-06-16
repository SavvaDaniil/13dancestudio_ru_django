from django.contrib import admin

from dancestudio13_ru.models import Teacher, TeacherAdmin
from dancestudio13_ru.models import Style, StyleAdmin
from dancestudio13_ru.models import Abonement, AbonementAdmin
from dancestudio13_ru.models import RentHall, RentHallAdmin
from dancestudio13_ru.models import Video, VideoAdmin
from dancestudio13_ru.models import DanceGroup, DanceGroupAdmin
from dancestudio13_ru.models import UserZayavka, UserZayavkaAdmin
# Register your models here.

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Abonement, AbonementAdmin)
admin.site.register(RentHall, RentHallAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(DanceGroup, DanceGroupAdmin)
admin.site.register(UserZayavka, UserZayavkaAdmin)
