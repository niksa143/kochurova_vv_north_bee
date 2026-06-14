"""
URL configuration for North_bee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from django.contrib.auth.decorators import login_required

from django.urls import path, include
from django.conf import settings  # PREP
from django.conf.urls.static import static  # PREP

from general.views import QuestCreateView
from history.views import HistoryListView

from home.views import HomeView
from quests.views import QuestUpdateView

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    
    path("", HomeView.as_view(), name="home"),

    path("quests/new",QuestCreateView.as_view(),name="new-quest"),
    path("quests/<int:pk>/update",QuestUpdateView.as_view(),name="quest-update"),
    path("quests/<int:pk>/history",HistoryListView.as_view(),name="quest-history"),

    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
