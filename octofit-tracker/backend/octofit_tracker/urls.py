"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers
from .views import (
    UserViewSet,
    TeamViewSet,
    ActivityViewSet,
    WorkoutViewSet,
    LeaderboardViewSet,
    api_root,
)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"teams", TeamViewSet)
router.register(r"activities", ActivityViewSet)
router.register(r"workouts", WorkoutViewSet)
router.register(r"leaderboards", LeaderboardViewSet)


# Get Codespace name for URL generation
CODESPACE_NAME = os.getenv("CODESPACE_NAME")

# 當在 Codespace 中運行時，使用 Codespace 的完整 domain 以避免 HTTPS 憑證問題
if CODESPACE_NAME:
    BASE_DOMAIN = f"https://{CODESPACE_NAME}-8000.app.github.dev"
    API_BASE_URL = f"{BASE_DOMAIN}/api"
    ROOT_REDIRECT = f"{BASE_DOMAIN}/api/"
else:
    # 使用相對路徑回退（可安全在任何 host 下運作）
    BASE_DOMAIN = None
    API_BASE_URL = "/api"
    ROOT_REDIRECT = "/api/"

urlpatterns = [
    path("admin/", admin.site.urls),
    # 由於這是 REST API 專案，將根路徑重定向到 /api/ 首頁（使用 Codespace domain 或本機回退）
    path("", RedirectView.as_view(url=ROOT_REDIRECT, permanent=False), name="home"),
    path("api/", api_root, name="api-root"),
    path("api/", include(router.urls)),
]
