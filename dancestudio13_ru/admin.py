from django.contrib import admin

from dancestudio13_ru.models import Teacher, TeacherAdmin
from dancestudio13_ru.models import Style, StyleAdmin
from dancestudio13_ru.models import Abonement, AbonementAdmin
from dancestudio13_ru.models import RentHall, RentHallAdmin
from dancestudio13_ru.models import Video, VideoAdmin
# Register your models here.

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Abonement, AbonementAdmin)
admin.site.register(RentHall, RentHallAdmin)
admin.site.register(Video, VideoAdmin)
