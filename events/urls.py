from django.urls import path

from events import views

urlpatterns = [
    path('competitor/', views.CompetitorsListView.as_view()),
    path('organizer_levels/', views.OrganizerLevelListView.as_view()),
    path('founding_types/', views.FoundingTypeListView.as_view())
]
