from dataclasses import dataclass
#from tkinter.messagebox import NO
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json

from dancestudio13_ru.Facade.TeacherFacade import TeacherFacade
from dancestudio13_ru.Facade.StyleFacade import StyleFacade
from dancestudio13_ru.Facade.AbonementFacade import AbonementFacade
from dancestudio13_ru.Facade.RentHallFacade import RentHallFacade
from dancestudio13_ru.Facade.DanceGroupFacade import DanceGroupFacade
from dancestudio13_ru.Facade.UserZayavkaFacade import UserZayavkaFacade
from dancestudio13_ru.ViewModel.JsonAnswerStatus import JsonAnswerStatus
from dancestudio13_ru.ViewModel.Style.StyleInfoViewModel import StyleInfoViewModel
from dancestudio13_ru.DTO.User.UserZayavkaDTO import UserZayavkaDTO
from dancestudio13_ru.DTO.Teacher.TeacherSearchDTO import TeacherSearchDTO
# Create your views here.
import dataclasses



def index(request):
    title = "Главная"
    teacherFacade = TeacherFacade()
    styleFacade = StyleFacade()
    abonementFacade = AbonementFacade()
    styleLiteViewModels = styleFacade.listAllLiteActive()
    abonementLiteViewModels = abonementFacade.listAllLiteActive()
    return render(
        request, 
        "index.html", 
        {
            "title" : title, 
            "styleLiteViewModels" : styleLiteViewModels,
            "abonementLiteViewModels" : abonementLiteViewModels
        }
    )


def teacherByShortLink(request, link_short: str = None):
    teacherFacade = TeacherFacade()
    teacherInfoViewModel = teacherFacade.getInfoByShortLink(link_short=link_short)
    if teacherInfoViewModel is None:
        return redirect("/teachers")
    title = teacherInfoViewModel.name
    return render(request, "teacher.html", {"title" : title, "teacherInfoViewModel" : teacherInfoViewModel})

def teacherById(request, id_of_teacher: int = 0):
    teacherFacade = TeacherFacade()
    teacherInfoViewModel = teacherFacade.getInfoById(id_of_teacher=id_of_teacher)
    if teacherInfoViewModel is None:
        return redirect("/teachers")
    title = teacherInfoViewModel.name
    return render(request, "teacher.html", {"title" : title, "teacherInfoViewModel" : teacherInfoViewModel})

def apiTeacherSearch(request):
    if request.method != "POST":
        return None
    teacherSearchDTO = TeacherSearchDTO(data=request.POST)
    if not teacherSearchDTO.is_valid():
        return None
    teacherFacade = TeacherFacade()
    jsonAnswerStatus = JsonAnswerStatus(status = "success", errors=None)
    teacherLiteViewModels = teacherFacade.search(
        offset=teacherSearchDTO.cleaned_data.get("offset"), 
        limit=teacherSearchDTO.cleaned_data.get("limit")
    )
    jsonAnswerStatus.teacherLiteViewModels = teacherLiteViewModels
    return JsonResponse(jsonAnswerStatus.__dict__)



def apiTeachersListAll(request):
    teacherFacade = TeacherFacade()
    teacherLiteViewModels = teacherFacade.listAllLiteActive()

    json_string = json.dumps(teacherLiteViewModels, ensure_ascii=False
                ).encode('utf8')
    return JsonResponse(
        {
            "status":"success",
            "teacherLiteViewModels":json.loads(
                json_string.decode()
            )
        })

def teachers(request):
    title = "Преподаватели"
    return render(
        request, 
        "teachers.html", 
        {
            "title" : title
        }
    )

def faq(request):
    title = "Часто задаваемые вопросы"
    return render(request, "faq.html", {"title" : title})

def contacts(request):
    title = "Контакты"
    return render(request, "contacts.html", {"title" : title})




def styleByShortLink(request, link_short: str = None):
    styleFacade = StyleFacade()
    styleInfoViewModel: StyleInfoViewModel = styleFacade.getInfoByShortLink(link_short = link_short)
    if not styleInfoViewModel:
        return redirect("/")
    title = styleInfoViewModel.name
    return render(request, "style.html", {"title":title, "styleInfoViewModel" : styleInfoViewModel})

def styleById(request, id_of_style: int = 0):
    styleFacade = StyleFacade()
    styleInfoViewModel: StyleInfoViewModel = styleFacade.getInfoById(id_of_style=id_of_style)
    if not styleInfoViewModel:
        return redirect("/")

    title = styleInfoViewModel.name
    return render(request, "style.html", {"title":title, "styleInfoViewModel" : styleInfoViewModel})




def rent_hall(request):
    rentHallFacade = RentHallFacade()
    rentHallLiteViewModels = rentHallFacade.listAllLiteActive()

    title = "Аренда залов"
    return render(request, "rent_hall.html", {"title":title, "rentHallLiteViewModels" : rentHallLiteViewModels})

def schedule(request):
    title = "Расписание"
    return render(request, "schedule.html", {"title":title})

def apiUserZayavka(request):
    if request.method != "POST":
        return JsonResponse()
    
    userZayavkaDTO = UserZayavkaDTO(request.POST)
    if not userZayavkaDTO.is_valid():
        jsonAnswerStatus = JsonAnswerStatus(status="error", errors="no_data")
        return JsonResponse(
            json.loads(json.dumps(jsonAnswerStatus))
        )
    
    userZayavkaFacade = UserZayavkaFacade()
    ip_address = None
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')
    
    if not userZayavkaFacade.create(name=userZayavkaDTO.cleaned_data.get("name"), phone=userZayavkaDTO.cleaned_data.get("phone"), ip_address=ip_address):
        jsonAnswerStatus = JsonAnswerStatus(status="error", errors="try_save")
        return JsonResponse(jsonAnswerStatus.__dict__)

    jsonAnswerStatus = JsonAnswerStatus(status="success", errors=None)
    return JsonResponse(jsonAnswerStatus.__dict__)


def video(request):
    return render(request, "video.html")

def apiDanceGroupSearch(request):
    danceGroupFacade = DanceGroupFacade()
    jsonAnswerStatus = JsonAnswerStatus(status="success", errors=None)
    jsonAnswerStatus.danceGroupLiteViewModels = danceGroupFacade.listAllLiteActive()
    return JsonResponse(jsonAnswerStatus.__dict__)