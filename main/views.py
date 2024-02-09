from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(["GET"])
def get_banner(request):
    banner = Banner.objects.last()
    ser = BannerSer(banner)
    return Response(ser.data)



@api_view(["GET"])
def get_about(request):
    about = About.objects.last()
    ser = AboutSer(about)
    return Response(ser.data)



@api_view(["GET"])
def get_service(request):
    service = Service.objects.last()
    ser = ServiceSer(service)
    return Response(ser.data)



@api_view(["GET"])
def get_project(request):
    project = Project.objects.last()
    ser = ProjectSer(project)
    return Response(ser.data)



@api_view(["GET"])
def get_our_team(request):
    our_team = Our_Team.objects.last()
    ser = Our_TeamSer(our_team)
    return Response(ser.data)




@api_view(["GET"])
def get_news(request):
    news = News.objects.last()
    ser = NewsSer(news)
    return Response(ser.data)


