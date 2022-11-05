from django.urls import path

from .views import CompetitorsListView

urlpatterns = [
    path('competitor/', CompetitorsListView.as_view()),
]