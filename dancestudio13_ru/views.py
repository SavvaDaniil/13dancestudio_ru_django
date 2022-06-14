from dataclasses import dataclass
#from tkinter.messagebox import NO
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json

from dancestudio13_ru.Facade.TeacherFacade import TeacherFacade
from dancestudio13_ru.Facade.StyleFacade import StyleFacade
from dancestudio13_ru.Facade.AbonementFacade import AbonementFacade
from dancestudio13_ru.Facade.RentHallFacade import RentHallFacade
from dancestudio13_ru.ViewModel.JsonAnswerStatus import JsonAnswerStatus
from dancestudio13_ru.ViewModel.Style.StyleInfoViewModel import StyleInfoViewModel
from dancestudio13_ru.DTO.User.UserZayavkaDTO import UserZayavkaDTO
from dancestudio13_ru.DTO.Teacher.TeacherSearchDTO import TeacherSearchDTO
# Create your views here.




def index(request):
    title = "Главная"
    teacherFacade = TeacherFacade()
    styleFacade = StyleFacade()
    abonementFacade = AbonementFacade()
    teacherLite6ViewModels = teacherFacade.listFirst6LiteActive()
    styleLiteViewModels = styleFacade.listAllLiteActive()
    abonementLiteViewModels = abonementFacade.listAllLiteActive()
    return render(
        request, 
        "index.html", 
        {
            "title" : title, 
            "teacherLite6ViewModels" : teacherLite6ViewModels,
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
    teacherSearchDTO = TeacherSearchDTO(request.POST)
    teacherFacade = TeacherFacade()
    jsonAnswerStatus = JsonAnswerStatus(status = "success")
    teacherInfoViewModel = teacherFacade.search(offset=teacherSearchDTO.offset, limit=teacherSearchDTO.limit)
    jsonAnswerStatus.teacherInfoViewModel = teacherInfoViewModel

    json_string = json.dumps(teacherInfoViewModel, ensure_ascii=False
                ).encode('utf8')
    return JsonResponse(
        {
            "status":"success",
            "teacherLiteViewModels":json.loads(
                json_string.decode()
            )
        })



def apiTeachersListAll(request):
    teacherFacade = TeacherFacade()
    teacherLiteViewModels = teacherFacade.listAllActiveLite()

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
    
    

    jsonAnswerStatus = JsonAnswerStatus(status="success")
    return JsonResponse(json.loads(json.dumps(jsonAnswerStatus)))




