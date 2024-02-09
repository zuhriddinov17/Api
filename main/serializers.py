from rest_framework import serializers
from .models import *


class BannerSer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class AboutSer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class ServiceSer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ProjectSer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"



class Our_TeamSer(serializers.ModelSerializer):
    class Meta:
        model = Our_Team
        fields = "__all__"


class NewsSer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"






