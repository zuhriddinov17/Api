from django.urls import path
from .views import *

urlpatterns = [
    path('get-banner/', get_banner),
    path('get-about/', get_about),
    path('get-service/', get_service),
    path('get-project/', get_project),
    path('get-our-team/', get_our_team),
    path('get-news/', get_news),
]