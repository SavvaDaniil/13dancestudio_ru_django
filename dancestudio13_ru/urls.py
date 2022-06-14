from django.urls import path
from sympy import im
from dancestudio13_ru import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index),
    path("api/user/zayavka", views.apiUserZayavka),
    path("api/teacher/list_all", views.apiTeachersListAll),
    #path("style/<str:link_short>", views.styleByShortLink),
    path("style/<int:id_of_style>", views.styleById),

    path("teachers", views.teachers),
    path("teacher/<str:link_short>", views.teacherByShortLink),
    path("teacher/<int:id_of_teacher>", views.teacherById),
    path("api/teacher/search", views.apiTeacherSearch),

    path("rent_hall", views.rent_hall),
    path("faq", views.faq),
    path("contacts", views.contacts),
    path("schedule", views.schedule)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)